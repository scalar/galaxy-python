# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import json
from typing import Mapping, cast

from .._types import HeadersLike
from .._utils import get_required_header
from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._webhook_verify import verify_webhook_signature
from ..types.parsed_webhook_event import ParsedWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise ValueError("Cannot verify a webhook with a key that decodes to an empty key")

        if not isinstance(headers, dict):
            headers = dict(headers)

        verify_webhook_signature(payload, headers, key)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def verify_signature(self, payload: str | bytes, headers: HeadersLike, *, key: str | bytes | None = None) -> None:
        """Verifies that `payload` was signed with the webhook key, raising when it was not.

        `key` defaults to the client's `webhook_secret`. A missing signature header raises too.
        """
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise ValueError("Cannot verify a webhook with a key that decodes to an empty key")

        signed_headers = {
            "webhook-id": get_required_header(headers, "webhook-id"),
            "webhook-timestamp": get_required_header(headers, "webhook-timestamp"),
            "webhook-signature": get_required_header(headers, "webhook-signature"),
        }
        verify_webhook_signature(payload, signed_headers, key)

    def parse_unsafe(self, payload: str) -> ParsedWebhookEvent:
        """Parses `payload` into a typed event without verifying its signature.

        Only use this for a payload whose signature was already verified, or in tests.
        """
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise ValueError("Cannot verify a webhook with a key that decodes to an empty key")

        if not isinstance(headers, dict):
            headers = dict(headers)

        verify_webhook_signature(payload, headers, key)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def verify_signature(self, payload: str | bytes, headers: HeadersLike, *, key: str | bytes | None = None) -> None:
        """Verifies that `payload` was signed with the webhook key, raising when it was not.

        `key` defaults to the client's `webhook_secret`. A missing signature header raises too.
        """
        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )
        try:
            from base64 import b64decode

            empty_key = (
                not key if isinstance(key, bytes) else not b64decode(key[6:] if key.startswith("whsec_") else key)
            )
        except ValueError:
            empty_key = False
        if empty_key:
            raise ValueError("Cannot verify a webhook with a key that decodes to an empty key")

        signed_headers = {
            "webhook-id": get_required_header(headers, "webhook-id"),
            "webhook-timestamp": get_required_header(headers, "webhook-timestamp"),
            "webhook-signature": get_required_header(headers, "webhook-signature"),
        }
        verify_webhook_signature(payload, signed_headers, key)

    def parse_unsafe(self, payload: str) -> ParsedWebhookEvent:
        """Parses `payload` into a typed event without verifying its signature.

        Only use this for a payload whose signature was already verified, or in tests.
        """
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )
