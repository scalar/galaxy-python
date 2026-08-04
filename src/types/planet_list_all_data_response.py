# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PlanetListAllDataResponse", "Meta"]


class Meta(BaseModel):

    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None

    next: Optional[str] = None



class PlanetListAllDataResponse(BaseModel):

    data: Optional[List[object]] = None

    meta: Optional[Meta] = None
