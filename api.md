# Scalar Galaxy Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Planets`](#planets)
  - [Get all planets](#get-all-planets)
  - [Create a planet](#create-a-planet)
  - [Get a planet](#get-a-planet)
  - [Update a planet](#update-a-planet)
  - [Delete a planet](#delete-a-planet)
  - [Upload an image to a planet](#upload-an-image-to-a-planet)
- [`CelestialBodies`](#celestialbodies)
  - [Create a celestial body](#create-a-celestial-body)
- [`Authentication`](#authentication)
  - [Create a user](#create-a-user)
  - [Get a token](#get-a-token)
  - [Get authenticated user](#get-authenticated-user)

## Setup

```python
import os

from scalar_galaxy import Galaxy

client = Galaxy(
    bearer_auth=os.environ.get("BEARER_AUTH"),
)
```

## `Planets`

### Get all planets

It's easy to say you know them all, but do you really? Retrieve all the planets and check whether you missed one.

| Direction | Type |
| --- | --- |
| Request | [`PlanetListAllDataParams`](./src/scalar_galaxy/types/planet_list_all_data_params.py) |
| Response | [`PlanetListAllDataResponse`](./src/scalar_galaxy/types/planet_list_all_data_response.py) |

```python
planet = client.planets.list_all_data(
    limit=10,
    offset=0,
)
```

### Create a planet

Time to play god and create a new planet. What do you think? Ah, don't think too much. What could go wrong anyway?

| Direction | Type |
| --- | --- |
| Request | [`PlanetCreateParams`](./src/scalar_galaxy/types/planet_create_params.py) |
| Response | [`Planet`](./src/scalar_galaxy/types/planet.py) |

```python
planet = client.planets.create(
    name="Mars",
)
```

### Get a planet

You'll better learn a little bit more about the planets. It might come in handy once space travel is available for everyone.

| Direction | Type |
| --- | --- |
| Response | [`Planet`](./src/scalar_galaxy/types/planet.py) |

```python
planet = client.planets.retrieve(
    planet_id=1,
)
```

### Update a planet

Sometimes you make mistakes, that's fine. No worries, you can update all planets.

| Direction | Type |
| --- | --- |
| Request | [`PlanetUpdateParams`](./src/scalar_galaxy/types/planet_update_params.py) |
| Response | [`Planet`](./src/scalar_galaxy/types/planet.py) |

```python
planet = client.planets.update(
    planet_id=1,
    name="Mars",
)
```

### Delete a planet

This endpoint was used to delete planets. Unfortunately, that caused a lot of trouble for planets with life. So, this endpoint is now deprecated and should not be used anymore.

```python
client.planets.delete(
    planet_id=1,
)
```

### Upload an image to a planet

Got a crazy good photo of a planet? Share it with the world!

| Direction | Type |
| --- | --- |
| Request | [`PlanetUploadImageParams`](./src/scalar_galaxy/types/planet_upload_image_params.py) |
| Response | [`PlanetUploadImageResponse`](./src/scalar_galaxy/types/planet_upload_image_response.py) |

```python
planet = client.planets.upload_image(
    planet_id=1,
)
```

## `CelestialBodies`

### Create a celestial body

Stars, moons, comets, the occasional rogue asteroid — if it glows or drifts through the void, you can add it here.

| Direction | Type |
| --- | --- |
| Request | [`CelestialBodyCreateParams`](./src/scalar_galaxy/types/celestial_body_create_params.py) |
| Response | [`CelestialBodyCreateResponse`](./src/scalar_galaxy/types/celestial_body_create_response.py) |

```python
celestial_body = client.celestial_bodies.create(
    name="Mars",
)
```

## `Authentication`

### Create a user

Time to create a user account, eh?

| Direction | Type |
| --- | --- |
| Request | [`AuthenticationCreateUserParams`](./src/scalar_galaxy/types/authentication_create_user_params.py) |
| Response | [`User`](./src/scalar_galaxy/types/user.py) |

```python
authentication = client.authentication.create_user(
    name="Marc",
    email="marc@scalar.com",
    password="i-love-scalar",
)
```

### Get a token

Yeah, this is the boring security stuff. Just get your super secret token and move on.

| Direction | Type |
| --- | --- |
| Request | [`AuthenticationCreateTokenParams`](./src/scalar_galaxy/types/authentication_create_token_params.py) |
| Response | [`AuthenticationCreateTokenResponse`](./src/scalar_galaxy/types/authentication_create_token_response.py) |

```python
authentication = client.authentication.create_token(
    email="marc@scalar.com",
    password="i-love-scalar",
)
```

### Get authenticated user

Find yourself they say. That's what you can do here.

| Direction | Type |
| --- | --- |
| Response | [`User`](./src/scalar_galaxy/types/user.py) |

```python
authentication = client.authentication.list_me()
```
