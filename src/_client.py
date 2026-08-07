# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import base64
import os
import threading
from typing import TYPE_CHECKING, Any, Mapping, cast
from typing_extensions import Literal, Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, is_mapping_t, get_async_library
from ._compat import cached_property
from ._exceptions import APIStatusError, GalaxyError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._version import __version__

if TYPE_CHECKING:
    from .resources import planets, celestial_bodies, authentication, webhooks
    from .resources.planets import PlanetsResource, AsyncPlanetsResource
    from .resources.celestial_bodies import CelestialBodiesResource, AsyncCelestialBodiesResource
    from .resources.authentication import AuthenticationResource, AsyncAuthenticationResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource

# Serializes lazy resource imports so concurrent cold access from multiple
# threads cannot deadlock on CPython import locks (see CPython 3.14).
_RESOURCE_IMPORT_LOCK = threading.RLock()

ENVIRONMENTS: dict[str, str] = {
    "production": "https://galaxy.scalar.com",
    "responds_with_your_request_data": "{protocol}://void.scalar.com/{path}",
}

__all__ = [
    "ENVIRONMENTS",
    "Galaxy",
    "AsyncGalaxy",
    "Client",
    "AsyncClient",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
]


class Galaxy(SyncAPIClient):
    # client options
    bearer_auth: str
    basic_auth_username: str
    basic_auth_password: str
    api_key_header: str
    api_key_query: str
    api_key_cookie: str
    o_auth2: str | None
    open_id_connect: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "responds_with_your_request_data"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Galaxy client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        - `basic_auth_username` from `BASIC_AUTH_USERNAME`
        - `basic_auth_password` from `BASIC_AUTH_PASSWORD`
        - `api_key_header` from `API_KEY_HEADER`
        - `api_key_query` from `API_KEY_QUERY`
        - `api_key_cookie` from `API_KEY_COOKIE`
        - `webhook_secret` from `SCALAR_WEBHOOK_SECRET`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise GalaxyError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        if basic_auth_username is None:
            basic_auth_username = os.environ.get("BASIC_AUTH_USERNAME")
        if basic_auth_username is None:
            raise GalaxyError(
                "The basic_auth_username client option must be set either by passing basic_auth_username to the client or by setting the BASIC_AUTH_USERNAME environment variable"
            )
        self.basic_auth_username = basic_auth_username
        if basic_auth_password is None:
            basic_auth_password = os.environ.get("BASIC_AUTH_PASSWORD")
        if basic_auth_password is None:
            raise GalaxyError(
                "The basic_auth_password client option must be set either by passing basic_auth_password to the client or by setting the BASIC_AUTH_PASSWORD environment variable"
            )
        self.basic_auth_password = basic_auth_password
        if api_key_header is None:
            api_key_header = os.environ.get("API_KEY_HEADER")
        if api_key_header is None:
            raise GalaxyError(
                "The api_key_header client option must be set either by passing api_key_header to the client or by setting the API_KEY_HEADER environment variable"
            )
        self.api_key_header = api_key_header
        if api_key_query is None:
            api_key_query = os.environ.get("API_KEY_QUERY")
        if api_key_query is None:
            raise GalaxyError(
                "The api_key_query client option must be set either by passing api_key_query to the client or by setting the API_KEY_QUERY environment variable"
            )
        self.api_key_query = api_key_query
        if api_key_cookie is None:
            api_key_cookie = os.environ.get("API_KEY_COOKIE")
        if api_key_cookie is None:
            raise GalaxyError(
                "The api_key_cookie client option must be set either by passing api_key_cookie to the client or by setting the API_KEY_COOKIE environment variable"
            )
        self.api_key_cookie = api_key_cookie
        if o_auth2 is None:
            o_auth2 = os.environ.get("SCALAR_O_AUTH2")
        self.o_auth2 = o_auth2
        if open_id_connect is None:
            open_id_connect = os.environ.get("SCALAR_OPEN_ID_CONNECT")
        self.open_id_connect = open_id_connect
        if webhook_secret is None:
            webhook_secret = os.environ.get("SCALAR_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret
        self._environment = environment
        base_url_env = os.environ.get("SCALAR_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # An explicit `base_url` wins over `environment` so callers can point a
            # pinned-environment client at a proxy or mock, and so `copy()` can pass
            # both the inherited host and the inherited environment without conflict.
            base_url = cast("str | httpx.URL", base_url)
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; the base URL environment variable and the `environment` argument are both set. Pass base_url=None to use the environment.",
                )
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        custom_headers_env = os.environ.get("SCALAR_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = Stream

    @cached_property
    def planets(self) -> "PlanetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import PlanetsResource
        return PlanetsResource(self)

    @cached_property
    def celestial_bodies(self) -> "CelestialBodiesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import CelestialBodiesResource
        return CelestialBodiesResource(self)

    @cached_property
    def authentication(self) -> "AuthenticationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResource
        return AuthenticationResource(self)

    @cached_property
    def webhooks(self) -> "WebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import WebhooksResource
        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> GalaxyWithRawResponse:
        return GalaxyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GalaxyWithStreamedResponse:
        return GalaxyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._basic_auth_header_auth,
            **self._bearer_auth_header_auth,
            **self._api_key_header_header_auth,
            **self._o_auth2_header_auth,
            **self._open_id_connect_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_query_query_auth,
        }

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_cookie_cookie_auth,
        }

    @property
    def _basic_auth_header_auth(self) -> dict[str, str]:
        username = self.basic_auth_username
        password = self.basic_auth_password
        if username is None or password is None:
            return {}
        value = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return {"Authorization": f"Basic {value}"}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_header_header_auth(self) -> dict[str, str]:
        value = self.api_key_header
        if value is None:
            return {}
        return {"X-API-Key": value}

    @property
    def _o_auth2_header_auth(self) -> dict[str, str]:
        value = self.o_auth2
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _open_id_connect_header_auth(self) -> dict[str, str]:
        value = self.open_id_connect
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_query_query_auth(self) -> dict[str, str]:
        value = self.api_key_query
        if value is None:
            return {}
        return {"api_key": value}

    @property
    def _api_key_cookie_cookie_auth(self) -> dict[str, str]:
        value = self.api_key_cookie
        if value is None:
            return {}
        return {"api_key": value}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return
        if params.get("api_key") is not None:
            return
        if cookies.get("api_key") is not None:
            return
        raise TypeError(
            "Could not resolve authentication method. Expected Authorization or X-API-Key or query api_key or cookie api_key to be set."
        )

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        webhook_secret: str | None = None,
        environment: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        copied_base_url = base_url if base_url is not None else self.base_url
        # Environment overrides must resolve their own URL instead of reusing this client's host.
        if environment is not None and base_url is None:
            copied_base_url = None
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            basic_auth_username=basic_auth_username or self.basic_auth_username,
            basic_auth_password=basic_auth_password or self.basic_auth_password,
            api_key_header=api_key_header or self.api_key_header,
            api_key_query=api_key_query or self.api_key_query,
            api_key_cookie=api_key_cookie or self.api_key_cookie,
            o_auth2=o_auth2 or self.o_auth2,
            open_id_connect=open_id_connect or self.open_id_connect,
            webhook_secret=webhook_secret or self.webhook_secret,
            environment=environment if environment is not None else self._environment,
            base_url=copied_base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGalaxy(AsyncAPIClient):
    # client options
    bearer_auth: str
    basic_auth_username: str
    basic_auth_password: str
    api_key_header: str
    api_key_query: str
    api_key_cookie: str
    o_auth2: str | None
    open_id_connect: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        webhook_secret: str | None = None,
        environment: Literal["production", "responds_with_your_request_data"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGalaxy client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_auth` from `BEARER_AUTH`
        - `basic_auth_username` from `BASIC_AUTH_USERNAME`
        - `basic_auth_password` from `BASIC_AUTH_PASSWORD`
        - `api_key_header` from `API_KEY_HEADER`
        - `api_key_query` from `API_KEY_QUERY`
        - `api_key_cookie` from `API_KEY_COOKIE`
        - `webhook_secret` from `SCALAR_WEBHOOK_SECRET`
        """
        if bearer_auth is None:
            bearer_auth = os.environ.get("BEARER_AUTH")
        if bearer_auth is None:
            raise GalaxyError(
                "The bearer_auth client option must be set either by passing bearer_auth to the client or by setting the BEARER_AUTH environment variable"
            )
        self.bearer_auth = bearer_auth
        if basic_auth_username is None:
            basic_auth_username = os.environ.get("BASIC_AUTH_USERNAME")
        if basic_auth_username is None:
            raise GalaxyError(
                "The basic_auth_username client option must be set either by passing basic_auth_username to the client or by setting the BASIC_AUTH_USERNAME environment variable"
            )
        self.basic_auth_username = basic_auth_username
        if basic_auth_password is None:
            basic_auth_password = os.environ.get("BASIC_AUTH_PASSWORD")
        if basic_auth_password is None:
            raise GalaxyError(
                "The basic_auth_password client option must be set either by passing basic_auth_password to the client or by setting the BASIC_AUTH_PASSWORD environment variable"
            )
        self.basic_auth_password = basic_auth_password
        if api_key_header is None:
            api_key_header = os.environ.get("API_KEY_HEADER")
        if api_key_header is None:
            raise GalaxyError(
                "The api_key_header client option must be set either by passing api_key_header to the client or by setting the API_KEY_HEADER environment variable"
            )
        self.api_key_header = api_key_header
        if api_key_query is None:
            api_key_query = os.environ.get("API_KEY_QUERY")
        if api_key_query is None:
            raise GalaxyError(
                "The api_key_query client option must be set either by passing api_key_query to the client or by setting the API_KEY_QUERY environment variable"
            )
        self.api_key_query = api_key_query
        if api_key_cookie is None:
            api_key_cookie = os.environ.get("API_KEY_COOKIE")
        if api_key_cookie is None:
            raise GalaxyError(
                "The api_key_cookie client option must be set either by passing api_key_cookie to the client or by setting the API_KEY_COOKIE environment variable"
            )
        self.api_key_cookie = api_key_cookie
        if o_auth2 is None:
            o_auth2 = os.environ.get("SCALAR_O_AUTH2")
        self.o_auth2 = o_auth2
        if open_id_connect is None:
            open_id_connect = os.environ.get("SCALAR_OPEN_ID_CONNECT")
        self.open_id_connect = open_id_connect
        if webhook_secret is None:
            webhook_secret = os.environ.get("SCALAR_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret
        self._environment = environment
        base_url_env = os.environ.get("SCALAR_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # An explicit `base_url` wins over `environment` so callers can point a
            # pinned-environment client at a proxy or mock, and so `copy()` can pass
            # both the inherited host and the inherited environment without conflict.
            base_url = cast("str | httpx.URL", base_url)
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; the base URL environment variable and the `environment` argument are both set. Pass base_url=None to use the environment.",
                )
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        custom_headers_env = os.environ.get("SCALAR_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}
        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self._idempotency_header = None
        self._default_stream_cls = AsyncStream

    @cached_property
    def planets(self) -> "AsyncPlanetsResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import AsyncPlanetsResource
        return AsyncPlanetsResource(self)

    @cached_property
    def celestial_bodies(self) -> "AsyncCelestialBodiesResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import AsyncCelestialBodiesResource
        return AsyncCelestialBodiesResource(self)

    @cached_property
    def authentication(self) -> "AsyncAuthenticationResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResource
        return AsyncAuthenticationResource(self)

    @cached_property
    def webhooks(self) -> "AsyncWebhooksResource":
        with _RESOURCE_IMPORT_LOCK:
            from .resources.webhooks import AsyncWebhooksResource
        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGalaxyWithRawResponse:
        return AsyncGalaxyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGalaxyWithStreamedResponse:
        return AsyncGalaxyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {
            **self._basic_auth_header_auth,
            **self._bearer_auth_header_auth,
            **self._api_key_header_header_auth,
            **self._o_auth2_header_auth,
            **self._open_id_connect_header_auth,
        }

    @override
    def _auth_query(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_query_query_auth,
        }

    @override
    def _auth_cookies(self, security: dict[str, bool]) -> dict[str, str]:
        _ = security
        return {
            **self._api_key_cookie_cookie_auth,
        }

    @property
    def _basic_auth_header_auth(self) -> dict[str, str]:
        username = self.basic_auth_username
        password = self.basic_auth_password
        if username is None or password is None:
            return {}
        value = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
        return {"Authorization": f"Basic {value}"}

    @property
    def _bearer_auth_header_auth(self) -> dict[str, str]:
        value = self.bearer_auth
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_header_header_auth(self) -> dict[str, str]:
        value = self.api_key_header
        if value is None:
            return {}
        return {"X-API-Key": value}

    @property
    def _o_auth2_header_auth(self) -> dict[str, str]:
        value = self.o_auth2
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _open_id_connect_header_auth(self) -> dict[str, str]:
        value = self.open_id_connect
        if value is None:
            return {}
        return {"Authorization": f"Bearer {value}"}

    @property
    def _api_key_query_query_auth(self) -> dict[str, str]:
        value = self.api_key_query
        if value is None:
            return {}
        return {"api_key": value}

    @property
    def _api_key_cookie_cookie_auth(self) -> dict[str, str]:
        value = self.api_key_cookie
        if value is None:
            return {}
        return {"api_key": value}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Scalar-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(
        self,
        headers: Headers,
        custom_headers: Headers,
        params: Mapping[str, object],
        cookies: Mapping[str, str],
    ) -> None:
        if headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return
        if headers.get("X-API-Key"):
            return
        if isinstance(custom_headers.get("X-API-Key"), Omit):
            return
        if params.get("api_key") is not None:
            return
        if cookies.get("api_key") is not None:
            return
        raise TypeError(
            "Could not resolve authentication method. Expected Authorization or X-API-Key or query api_key or cookie api_key to be set."
        )

    def copy(
        self,
        *,
        bearer_auth: str | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
        api_key_cookie: str | None = None,
        o_auth2: str | None = None,
        open_id_connect: str | None = None,
        webhook_secret: str | None = None,
        environment: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """Create a new client reusing this client's options with optional overrides."""
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")
        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")
        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers
        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query
        http_client = http_client or self._client
        copied_base_url = base_url if base_url is not None else self.base_url
        # Environment overrides must resolve their own URL instead of reusing this client's host.
        if environment is not None and base_url is None:
            copied_base_url = None
        return self.__class__(
            bearer_auth=bearer_auth or self.bearer_auth,
            basic_auth_username=basic_auth_username or self.basic_auth_username,
            basic_auth_password=basic_auth_password or self.basic_auth_password,
            api_key_header=api_key_header or self.api_key_header,
            api_key_query=api_key_query or self.api_key_query,
            api_key_cookie=api_key_cookie or self.api_key_cookie,
            o_auth2=o_auth2 or self.o_auth2,
            open_id_connect=open_id_connect or self.open_id_connect,
            webhook_secret=webhook_secret or self.webhook_secret,
            environment=environment if environment is not None else self._environment,
            base_url=copied_base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            _strict_response_validation=self._strict_response_validation,
            **_extra_kwargs,
        )

    with_options = copy

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)
        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)
        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)
        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)
        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)
        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)
        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GalaxyWithRawResponse:
    _client: Galaxy

    def __init__(self, client: Galaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> planets.PlanetsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import PlanetsResourceWithRawResponse
        return PlanetsResourceWithRawResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> celestial_bodies.CelestialBodiesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import CelestialBodiesResourceWithRawResponse
        return CelestialBodiesResourceWithRawResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> authentication.AuthenticationResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResourceWithRawResponse
        return AuthenticationResourceWithRawResponse(self._client.authentication)


class AsyncGalaxyWithRawResponse:
    _client: AsyncGalaxy

    def __init__(self, client: AsyncGalaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> planets.AsyncPlanetsResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import AsyncPlanetsResourceWithRawResponse
        return AsyncPlanetsResourceWithRawResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> celestial_bodies.AsyncCelestialBodiesResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import AsyncCelestialBodiesResourceWithRawResponse
        return AsyncCelestialBodiesResourceWithRawResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> authentication.AsyncAuthenticationResourceWithRawResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResourceWithRawResponse
        return AsyncAuthenticationResourceWithRawResponse(self._client.authentication)


class GalaxyWithStreamedResponse:
    _client: Galaxy

    def __init__(self, client: Galaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> planets.PlanetsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import PlanetsResourceWithStreamingResponse
        return PlanetsResourceWithStreamingResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> celestial_bodies.CelestialBodiesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import CelestialBodiesResourceWithStreamingResponse
        return CelestialBodiesResourceWithStreamingResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> authentication.AuthenticationResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AuthenticationResourceWithStreamingResponse
        return AuthenticationResourceWithStreamingResponse(self._client.authentication)


class AsyncGalaxyWithStreamedResponse:
    _client: AsyncGalaxy

    def __init__(self, client: AsyncGalaxy) -> None:
        self._client = client

    @cached_property
    def planets(self) -> planets.AsyncPlanetsResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.planets import AsyncPlanetsResourceWithStreamingResponse
        return AsyncPlanetsResourceWithStreamingResponse(self._client.planets)

    @cached_property
    def celestial_bodies(self) -> celestial_bodies.AsyncCelestialBodiesResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.celestial_bodies import AsyncCelestialBodiesResourceWithStreamingResponse
        return AsyncCelestialBodiesResourceWithStreamingResponse(self._client.celestial_bodies)

    @cached_property
    def authentication(self) -> authentication.AsyncAuthenticationResourceWithStreamingResponse:
        with _RESOURCE_IMPORT_LOCK:
            from .resources.authentication import AsyncAuthenticationResourceWithStreamingResponse
        return AsyncAuthenticationResourceWithStreamingResponse(self._client.authentication)


# Alias names for the documented `Client` / `AsyncClient` symbols.
Client = Galaxy
AsyncClient = AsyncGalaxy
