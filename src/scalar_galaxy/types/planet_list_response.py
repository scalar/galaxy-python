# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

from .planet import Planet

__all__ = ["PlanetListResponse", "Meta"]


class Meta(BaseModel):
    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None

    next: Optional[str] = None


class PlanetListResponse(BaseModel):
    data: Optional[List[Planet]] = None

    meta: Optional[Meta] = None
