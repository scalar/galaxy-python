"""Verifies Standard Webhooks signatures with the standard library alone.

A delivery is signed with an HMAC (SHA-256 unless the helper names SHA-1 or SHA-512) over
`"<id>.<timestamp>.<body>"`, keyed with the base64-decoded secret, and the signature header carries
one or more space-separated `v1,<base64 signature>` entries. Each helper passes in its own algorithm,
header names (`webhook-id`, `webhook-timestamp` and `webhook-signature` by default) and replay
window. Ed25519 and RSA signatures cannot be checked here, so such a delivery is always refused. With
the default settings this module checks a delivery the way the `standardwebhooks` 1.x package does,
with the same secret decoding, header lookup, signed content, tolerance window and error messages,
and like the library's `verify` it returns the JSON-decoded body once a signature matches. A refused
delivery raises this package's `WebhookVerificationError`, which also subclasses the library's class
of that name whenever the library is installed, so handlers written against it still catch it.
An empty secret raises `ValueError` where the library raised `EmptyWebhookSecretError`; the generated
webhook methods refuse such a key before calling in here. A delivery without its signed headers raises
`WebhookMissingHeadersError`, a `WebhookVerificationError` that is also a `ValueError`, so either
`except` clause catches it.
"""

from __future__ import annotations

import hmac
import json
import base64
import hashlib
from math import floor
from typing import Mapping
from datetime import datetime, timezone, timedelta

from ._exceptions import WebhookVerificationError, WebhookMissingHeadersError

__all__ = ["verify_webhook_signature", "refuse_unverifiable_algorithm"]

_SECRET_PREFIX = "whsec_"

# Deliveries stamped more than five minutes (unless a helper allows another window) before or after the
# local clock are refused, so a captured delivery cannot be replayed later and a forward-dated one cannot
# outlive the window either.
_DEFAULT_TOLERANCE_SECONDS = 300

# The HMAC digests a signature can be checked with, keyed by the algorithm name the SDK config spells.
_HMAC_DIGESTS = {
    "hmac-sha1": hashlib.sha1,
    "hmac-sha256": hashlib.sha256,
    "hmac-sha512": hashlib.sha512,
}


def _utcnow() -> datetime:
    """The current time, in UTC; a function so tests can pin the clock."""
    return datetime.now(tz=timezone.utc)


def _decode_secret(key: str | bytes) -> bytes:
    """Turns the configured key into the HMAC key bytes.

    A `str` key is a base64 secret, optionally prefixed with `whsec_` as dashboards display it; `bytes`
    are already the raw HMAC key and are used as given. Two `=` are appended before decoding so an
    unpadded secret decodes too: `b64decode` ignores padding beyond what the input needs, so a secret
    that was already padded decodes to the same bytes. Decoding is not strict, as in the library:
    ASCII characters outside the base64 alphabet are dropped, so a secret that is not base64 usually
    decodes to some other key and simply fails to verify. A non-ASCII secret, or one left with a length
    no padding can fix, raises `ValueError` (the latter as its `binascii.Error` subclass).
    """
    if isinstance(key, str):
        if key.startswith(_SECRET_PREFIX):
            key = key[len(_SECRET_PREFIX) :]
        key = base64.b64decode(key + "==")

    # An empty HMAC key is one anyone can sign with, so it can never verify a delivery.
    if not key:
        raise ValueError("webhook secret may not be empty")
    return key


def refuse_unverifiable_algorithm(algorithm: str, decode_method: str | None = None) -> None:
    """Raises `WebhookVerificationError` unless `algorithm` is an HMAC this module can check.

    A helper signed with `ed25519` or `rsa-sha256` calls this first, ahead of its key and header checks,
    so the caller learns that the SDK cannot verify the delivery at all, rather than that a key or a
    header is missing. `decode_method` names the helper's method that decodes without verifying.
    """
    if algorithm in _HMAC_DIGESTS:
        return
    decode = f"then decode the payload with {decode_method}()" if decode_method else "then decode the payload"
    raise WebhookVerificationError(
        f"Cannot verify a webhook signed with {algorithm}: this SDK checks only hmac-sha1, hmac-sha256 and "
        f"hmac-sha512 signatures, so the delivery was not accepted. Verify the signature yourself, {decode}."
    )


def _parse_timestamp(header: str, tolerance_seconds: int) -> datetime:
    """Reads the timestamp header (seconds since the epoch) and refuses one outside the tolerance window."""
    now = _utcnow()
    tolerance = timedelta(seconds=tolerance_seconds)
    try:
        timestamp = datetime.fromtimestamp(float(header), tz=timezone.utc)
    except Exception as exc:
        raise WebhookVerificationError("Invalid Signature Headers") from exc

    if timestamp < now - tolerance:
        raise WebhookVerificationError("Message timestamp too old")
    if timestamp > now + tolerance:
        raise WebhookVerificationError("Message timestamp too new")
    return timestamp


def verify_webhook_signature(
    payload: str | bytes,
    headers: Mapping[str, str],
    key: str | bytes,
    *,
    algorithm: str = "hmac-sha256",
    id_header: str = "webhook-id",
    timestamp_header: str = "webhook-timestamp",
    signature_header: str = "webhook-signature",
    tolerance_seconds: int = _DEFAULT_TOLERANCE_SECONDS,
    decode_method: str | None = None,
) -> object:
    """Returns the JSON-decoded `payload` once it carries a valid, fresh signature made with `key`.

    The keyword arguments are the helper's signature scheme: the HMAC `algorithm` (`hmac-sha1`,
    `hmac-sha256` or `hmac-sha512`), the three signed header names and the replay window in seconds.
    Any other algorithm (`ed25519`, `rsa-sha256`) cannot be checked with the standard library, so the
    delivery is refused with `WebhookVerificationError` before anything else is read, never accepted
    unverified; `decode_method` names the helper's method that decodes a payload without verifying it,
    which the message points the caller at.

    A missing header, a timestamp outside the tolerance or no matching signature raises
    `WebhookVerificationError`; for a missing header it is the `WebhookMissingHeadersError` subclass,
    which is also a `ValueError`, saying `Could not find <name> header` for an absent one and
    `Missing required headers` for an empty one. Input the library also rejected with something else raises the same
    `ValueError` it did: a signature entry that is not a `<version>,<signature>` pair, an undecodable
    signature, a `bytes` payload that is not UTF-8, or a signed body that is not JSON. An empty secret
    raises `ValueError` too, where the library raised `EmptyWebhookSecretError`.

    `headers` is matched case-insensitively. A `bytes` payload is decoded as UTF-8 and signed as text,
    exactly as a `str` payload is, so either form of the same body verifies alike.
    """
    refuse_unverifiable_algorithm(algorithm, decode_method)
    digest = _HMAC_DIGESTS[algorithm]

    secret = _decode_secret(key)
    body = payload if isinstance(payload, str) else payload.decode()

    lowered = {name.lower(): value for name, value in headers.items()}
    # An absent header is named, as `get_required_header` names it; one that is present but empty is
    # refused below with the library's message.
    for name in (id_header, timestamp_header, signature_header):
        if lowered.get(name.lower()) is None:
            raise WebhookMissingHeadersError(f"Could not find {name} header")
    msg_id = lowered.get(id_header.lower())
    msg_timestamp = lowered.get(timestamp_header.lower())
    msg_signature = lowered.get(signature_header.lower())
    if not (msg_id and msg_timestamp and msg_signature):
        raise WebhookMissingHeadersError("Missing required headers")

    timestamp = _parse_timestamp(msg_timestamp, tolerance_seconds)
    # The signed content uses the whole seconds of the parsed timestamp, not the header text, so a
    # header such as `1614265330.0` is checked against the signature made over `1614265330`.
    signed_content = f"{msg_id}.{floor(timestamp.timestamp())}.{body}".encode()
    expected = hmac.new(secret, signed_content, digest).digest()

    # A sender rotating its secret signs with both keys, so any one `v1` entry matching is enough;
    # entries for other signature versions are skipped. An entry that is not a `<version>,<signature>`
    # pair raises the `ValueError` unpacking raises, as one whose signature leaves an unfixable base64
    # length does; other stray characters are dropped by the lenient decoder and the entry just fails.
    # Entries are checked in order, so a malformed one ahead of a valid one raises before it is reached.
    for entry in msg_signature.split(" "):
        version, signature = entry.split(",")
        if version != "v1":
            continue
        # `compare_digest` takes the same time wherever the first differing byte is, so the response
        # time cannot be used to recover a valid signature one byte at a time.
        if hmac.compare_digest(expected, base64.b64decode(signature)):
            return json.loads(body)

    raise WebhookVerificationError("No matching signature found")
