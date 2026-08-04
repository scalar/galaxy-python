# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import json
from typing import Mapping, cast

from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import GalaxyError
from ..types.parsed_webhook_event import ParsedWebhookEvent

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise GalaxyError("You need to install `scalar-galaxy[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooksResource(AsyncAPIResource):
    def unwrap(self, payload: str, *, headers: Mapping[str, str], key: str | bytes | None = None) -> ParsedWebhookEvent:
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise GalaxyError("You need to install `scalar-galaxy[webhooks]` to use this method") from exc

        if key is None:
            key = self._client.webhook_secret
            if key is None:
                raise ValueError(
                    "Cannot verify a webhook without a key on either the client's webhook_secret or passed in as an argument"
                )

        if not isinstance(headers, dict):
            headers = dict(headers)

        Webhook(key).verify(payload, headers)

        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )
