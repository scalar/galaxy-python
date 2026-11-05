"""Verifies Standard Webhooks signatures with the standard library alone.

A delivery is signed with HMAC-SHA256 over `"<webhook-id>.<webhook-timestamp>.<body>"`, keyed with
the base64-decoded secret, and the `webhook-signature` header carries one or more space-separated
`v1,<base64 signature>` entries. This module checks a delivery the way the `standardwebhooks` 1.x
package does, with the same secret decoding, header lookup, signed content, tolerance window and error
messages, and like the library's `verify` it returns the JSON-decoded body once a signature matches. A
refused delivery raises this package's `WebhookVerificationError`, which also subclasses the library's
class of that name whenever the library is installed, so handlers written against it still catch it.
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

__all__ = ["verify_webhook_signature"]

_SECRET_PREFIX = "whsec_"

# Deliveries stamped more than five minutes before or after the local clock are refused, so a captured
# delivery cannot be replayed later and a forward-dated one cannot outlive the window either.
_TOLERANCE = timedelta(minutes=5)


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


def _parse_timestamp(header: str) -> datetime:
    """Reads `webhook-timestamp` (seconds since the epoch) and refuses one outside the tolerance window."""
    now = _utcnow()
    try:
        timestamp = datetime.fromtimestamp(float(header), tz=timezone.utc)
    except Exception as exc:
        raise WebhookVerificationError("Invalid Signature Headers") from exc

    if timestamp < now - _TOLERANCE:
        raise WebhookVerificationError("Message timestamp too old")
    if timestamp > now + _TOLERANCE:
        raise WebhookVerificationError("Message timestamp too new")
    return timestamp


def verify_webhook_signature(payload: str | bytes, headers: Mapping[str, str], key: str | bytes) -> object:
    """Returns the JSON-decoded `payload` once it carries a valid, fresh signature made with `key`.

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
    secret = _decode_secret(key)
    body = payload if isinstance(payload, str) else payload.decode()

    lowered = {name.lower(): value for name, value in headers.items()}
    # An absent header is named, as `get_required_header` names it; one that is present but empty is
    # refused below with the library's message.
    for name in ("webhook-id", "webhook-timestamp", "webhook-signature"):
        if lowered.get(name) is None:
            raise WebhookMissingHeadersError(f"Could not find {name} header")
    msg_id = lowered.get("webhook-id")
    msg_timestamp = lowered.get("webhook-timestamp")
    msg_signature = lowered.get("webhook-signature")
    if not (msg_id and msg_timestamp and msg_signature):
        raise WebhookMissingHeadersError("Missing required headers")

    timestamp = _parse_timestamp(msg_timestamp)
    # The signed content uses the whole seconds of the parsed timestamp, not the header text, so a
    # header such as `1614265330.0` is checked against the signature made over `1614265330`.
    signed_content = f"{msg_id}.{floor(timestamp.timestamp())}.{body}".encode()
    expected = hmac.new(secret, signed_content, hashlib.sha256).digest()

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
