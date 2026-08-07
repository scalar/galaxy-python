# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Iterable, Optional, Union
from datetime import datetime
from typing_extensions import Annotated, Literal, Required, TypedDict
from .._types import SequenceNotStr

from .._utils import PropertyInfo

from .user_param import UserParam

__all__ = ["PlanetUpdateParams", "PhysicalProperties", "PhysicalPropertiesTemperature", "Atmosphere", "Satellite"]


class PlanetUpdateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    type: Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"]

    habitability_index: Annotated[float, PropertyInfo(alias="habitabilityIndex")]
    """A score from 0 to 1 indicating potential habitability"""

    physical_properties: Annotated[PhysicalProperties, PropertyInfo(alias="physicalProperties")]

    atmosphere: Iterable[Atmosphere]
    """Atmospheric composition"""

    discovered_at: Annotated[Union[str, datetime], PropertyInfo(alias="discoveredAt", format="iso8601")]

    image: Optional[str]

    satellites: Iterable[Satellite]

    creator: UserParam
    """A user"""

    tags: SequenceNotStr[str]

    success_callback_url: Annotated[str, PropertyInfo(alias="successCallbackUrl")]
    """URL which gets invoked upon a successful operation"""

    failure_callback_url: Annotated[str, PropertyInfo(alias="failureCallbackUrl")]
    """URL which gets invoked upon a failed operation"""


class Satellite(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    diameter: float
    """Diameter in kilometers"""

    type: Literal["moon", "asteroid", "comet"]

    orbit: object


class Atmosphere(TypedDict, total=False):
    compound: str

    percentage: float


class PhysicalPropertiesTemperature(TypedDict, total=False):
    min: float
    """Minimum temperature in Kelvin"""

    max: float
    """Maximum temperature in Kelvin"""

    average: float
    """Average temperature in Kelvin"""


class PhysicalProperties(TypedDict, total=False):
    mass: float
    """Mass in Earth masses (must be greater than 0)"""

    radius: float
    """Radius in Earth radii (must be greater than 0)"""

    gravity: float
    """Surface gravity in Earth g"""

    temperature: PhysicalPropertiesTemperature
