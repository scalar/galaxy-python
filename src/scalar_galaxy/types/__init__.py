# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from . import (
    planet,
    new_planet_webhook_event,
)
from .. import _compat

from .user import User as User
from .celestial_body import CelestialBody as CelestialBody
from .planet import Planet as Planet
from .user_param import UserParam as UserParam
from .planet_param import PlanetParam as PlanetParam
from .new_planet_webhook_event import NewPlanetWebhookEvent as NewPlanetWebhookEvent
from .parsed_webhook_event import ParsedWebhookEvent as ParsedWebhookEvent
from .planet_list_all_data_response import PlanetListAllDataResponse as PlanetListAllDataResponse
from .planet_list_all_data_params import PlanetListAllDataParams as PlanetListAllDataParams
from .planet_create_params import PlanetCreateParams as PlanetCreateParams
from .planet_update_params import PlanetUpdateParams as PlanetUpdateParams
from .planet_delte_image_response import PlanetDelteImageResponse as PlanetDelteImageResponse
from .planet_delte_image_params import PlanetDelteImageParams as PlanetDelteImageParams
from .celestial_body_create_response import CelestialBodyCreateResponse as CelestialBodyCreateResponse
from .celestial_body_create_params import CelestialBodyCreateParams as CelestialBodyCreateParams
from .authentication_create_user_params import AuthenticationCreateUserParams as AuthenticationCreateUserParams
from .authentication_create_token_response import AuthenticationCreateTokenResponse as AuthenticationCreateTokenResponse
from .authentication_create_token_params import AuthenticationCreateTokenParams as AuthenticationCreateTokenParams

# Rebuild the models that carry forward references only after every module is imported, so the
# names their annotations mention are all bound by the time the model schema is built.
if _compat.PYDANTIC_V1:
    planet.Planet.update_forward_refs()  # type: ignore
    new_planet_webhook_event.NewPlanetWebhookEvent.update_forward_refs()  # type: ignore
else:
    planet.Planet.model_rebuild(_parent_namespace_depth=0)
    new_planet_webhook_event.NewPlanetWebhookEvent.model_rebuild(_parent_namespace_depth=0)
