# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional, Union
from typing_extensions import Annotated, Literal, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

from .planet import Planet

__all__ = ["CelestialBody", "Satellite"]

class Satellite(BaseModel):

    id: Optional[int] = None

    name: str

    description: Optional[str] = None

    diameter: Optional[float] = None
    """Diameter in kilometers"""

    type: Optional[Literal["moon", "asteroid", "comet"]] = None

    orbit: Optional[object] = None



CelestialBody: TypeAlias = Annotated[Union[Planet, Satellite], PropertyInfo(discriminator="type")]
