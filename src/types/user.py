# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    """A user"""

    id: Optional[int] = None

    name: Optional[str] = None
