# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .planet_param import PlanetParam
from .user_param import UserParam

__all__ = ["CelestialBodyCreateParams", "Planet", "PlanetPhysicalProperties", "PlanetPhysicalPropertiesTemperature", "PlanetAtmosphere", "PlanetSatellite", "Satellite", "SatelliteOrbit"]

class SatelliteOrbit(TypedDict, total=False):

    planet: PlanetParam
    """A planet in the Scalar Galaxy"""

    orbital_period: Annotated[float, PropertyInfo(alias="orbitalPeriod")]
    """Orbital period in Earth days"""

    distance: float
    """Average distance from the planet in kilometers"""

class Satellite(TypedDict, total=False):

    name: Required[str]

    description: Optional[str]

    diameter: float
    """Diameter in kilometers"""

    type: Literal["moon", "asteroid", "comet"]

    orbit: SatelliteOrbit

class PlanetSatellite(TypedDict, total=False):

    name: Required[str]

    description: Optional[str]

    diameter: float
    """Diameter in kilometers"""

    type: Literal["moon", "asteroid", "comet"]

    orbit: SatelliteOrbit

class PlanetAtmosphere(TypedDict, total=False):

    compound: str

    percentage: float

class PlanetPhysicalPropertiesTemperature(TypedDict, total=False):

    min: float
    """Minimum temperature in Kelvin"""

    max: float
    """Maximum temperature in Kelvin"""

    average: float
    """Average temperature in Kelvin"""

class PlanetPhysicalProperties(TypedDict, total=False):

    mass: float
    """Mass in Earth masses (must be greater than 0)"""

    radius: float
    """Radius in Earth radii (must be greater than 0)"""

    gravity: float
    """Surface gravity in Earth g"""

    temperature: PlanetPhysicalPropertiesTemperature

class Planet(TypedDict, total=False):

    name: Required[str]

    description: Optional[str]

    type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"]

    habitability_index: Annotated[float, PropertyInfo(alias="habitabilityIndex")]
    """A score from 0 to 1 indicating potential habitability"""

    physical_properties: Annotated[PlanetPhysicalProperties, PropertyInfo(alias="physicalProperties")]

    atmosphere: Iterable[PlanetAtmosphere]
    """Atmospheric composition"""

    discovered_at: Annotated[Union[str, datetime], PropertyInfo(alias="discoveredAt", format="iso8601")]

    image: Optional[str]

    satellites: Iterable[PlanetSatellite]

    creator: UserParam
    """A user"""

    tags: SequenceNotStr[str]

    success_callback_url: Annotated[str, PropertyInfo(alias="successCallbackUrl")]
    """URL which gets invoked upon a successful operation"""

    failure_callback_url: Annotated[str, PropertyInfo(alias="failureCallbackUrl")]
    """URL which gets invoked upon a failed operation"""



CelestialBodyCreateParams: TypeAlias = Union[Planet, Satellite]
