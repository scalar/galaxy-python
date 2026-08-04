# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .user import User

__all__ = ["Planet", "PhysicalProperties", "PhysicalPropertiesTemperature", "Atmosphere"]


class Atmosphere(BaseModel):

    compound: Optional[str] = None

    percentage: Optional[float] = None

class PhysicalPropertiesTemperature(BaseModel):

    min: Optional[float] = None
    """Minimum temperature in Kelvin"""

    max: Optional[float] = None
    """Maximum temperature in Kelvin"""

    average: Optional[float] = None
    """Average temperature in Kelvin"""

class PhysicalProperties(BaseModel):

    mass: Optional[float] = None
    """Mass in Earth masses (must be greater than 0)"""

    radius: Optional[float] = None
    """Radius in Earth radii (must be greater than 0)"""

    gravity: Optional[float] = None
    """Surface gravity in Earth g"""

    temperature: Optional[PhysicalPropertiesTemperature] = None



class Planet(BaseModel):
    """A planet in the Scalar Galaxy"""

    id: int

    name: str

    description: Optional[str] = None

    type: Optional[Literal["terrestrial", "gas_giant", "ice_giant", "dwarf", "super_earth"]] = None

    habitability_index: Optional[float] = FieldInfo(alias="habitabilityIndex", default=None)
    """A score from 0 to 1 indicating potential habitability"""

    physical_properties: Optional[PhysicalProperties] = FieldInfo(alias="physicalProperties", default=None)

    atmosphere: Optional[List[Atmosphere]] = None
    """Atmospheric composition"""

    discovered_at: Optional[datetime] = FieldInfo(alias="discoveredAt", default=None)

    image: Optional[str] = None

    satellites: Optional[List[object]] = None

    creator: Optional[User] = None
    """A user"""

    tags: Optional[List[str]] = None

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)

    success_callback_url: Optional[str] = FieldInfo(alias="successCallbackUrl", default=None)
    """URL which gets invoked upon a successful operation"""

    failure_callback_url: Optional[str] = FieldInfo(alias="failureCallbackUrl", default=None)
    """URL which gets invoked upon a failed operation"""
