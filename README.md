# Scalar Galaxy

This library provides convenient access to the Scalar Galaxy REST API from Python.

The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](./api.md)
- [Async](#async)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install scalar-galaxy
```

<br />

## Usage

```python
import os

from scalar_galaxy import Galaxy

client = Galaxy(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)

planet = client.planets.list_all_data(
    limit=10,
    offset=0,
)

print(planet)
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncGalaxy`) exposing the same resource tree with `await`.

```python
import asyncio

from scalar_galaxy import AsyncGalaxy

async def main() -> None:
    client = AsyncGalaxy()
    planet = await client.planets.list_all_data(
        limit=10,
        offset=0,
    )

asyncio.run(main())
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `string \| provider` | - | JWT Bearer token authentication Defaults to BEARER_AUTH. |
| `basic_auth_username` | `string \| provider` | - | Basic HTTP authentication Defaults to BASIC_AUTH_USERNAME. |
| `api_key_header` | `string \| provider` | - | API key request header Defaults to API_KEY_HEADER. |
| `api_key_query` | `string \| provider` | - | API key query parameter Defaults to API_KEY_QUERY. |
| `api_key_cookie` | `string \| provider` | - | API key browser cookie Defaults to API_KEY_COOKIE. |
| `o_auth2` | `string \| provider` | - | OAuth 2.0 authentication Defaults to SCALAR_O_AUTH2. |
| `open_id_connect` | `string \| provider` | - | OpenID Connect Authentication Defaults to SCALAR_OPEN_ID_CONNECT. |

Declared schemes:

- `bearerAuth` bearer token
- `basicAuth` basic authentication
- `apiKeyHeader` API key in header `X-API-Key`
- `apiKeyQuery` API key in query `api_key`
- `apiKeyCookie` API key in cookie `api_key`
- `oAuth2` OAuth2/OpenID Connect
- `openIdConnect` OAuth2/OpenID Connect

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from scalar_galaxy import APIStatusError

try:
    planet = client.planets.list_all_data(
        limit=10,
        offset=0,
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `400`, `401`, `403`, `404`, `409`, `422`, `429`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from scalar_galaxy import Galaxy

client = Galaxy(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `bearer_auth` | `str \| None` | `os.environ.get("BEARER_AUTH")` | JWT Bearer token authentication |
| `basic_auth_username` | `str \| None` | `os.environ.get("BASIC_AUTH_USERNAME")` | Basic HTTP authentication |
| `api_key_header` | `str \| None` | `os.environ.get("API_KEY_HEADER")` | API key request header |
| `api_key_query` | `str \| None` | `os.environ.get("API_KEY_QUERY")` | API key query parameter |
| `api_key_cookie` | `str \| None` | `os.environ.get("API_KEY_COOKIE")` | API key browser cookie |
| `o_auth2` | `str \| None` | `os.environ.get("SCALAR_O_AUTH2")` | OAuth 2.0 authentication |
| `open_id_connect` | `str \| None` | `os.environ.get("SCALAR_OPEN_ID_CONNECT")` | OpenID Connect Authentication |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `SCALAR_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `scalar_galaxy` logger.

<br />

## Requirements

- Python 3.8 or newer

Powered by Scalar.
