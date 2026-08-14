---
name: scalar-galaxy-python-sdk
description: "Python SDK for Scalar Galaxy API. Use when writing Python code that calls Scalar Galaxy API with the scalar-galaxy package: installing it, constructing and authenticating the client, and calling API operations."
---

# Scalar Galaxy Python SDK

Generated Python client for Scalar Galaxy API, published as `scalar-galaxy`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install scalar-galaxy
```

## Client setup and authentication

```python
import os

from scalar_galaxy import Galaxy

client = Galaxy(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `bearer_auth` (env: `BEARER_AUTH`) — JWT Bearer token authentication
- `basic_auth_username` (env: `BASIC_AUTH_USERNAME`) — Basic HTTP authentication
- `api_key_header` (env: `API_KEY_HEADER`) — API key request header
- `api_key_query` (env: `API_KEY_QUERY`) — API key query parameter
- `api_key_cookie` (env: `API_KEY_COOKIE`) — API key browser cookie
- `o_auth2` (env: `SCALAR_O_AUTH2`) — OAuth 2.0 authentication
- `open_id_connect` (env: `SCALAR_OPEN_ID_CONNECT`) — OpenID Connect Authentication

## Calling operations

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

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](../../../api.md) before writing a call.

## Error handling

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

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](../../../README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](../../../api.md) — complete catalogue of every operation with request and response types.
