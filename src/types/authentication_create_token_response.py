# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthenticationCreateTokenResponse"]


class AuthenticationCreateTokenResponse(BaseModel):
    token: Optional[str] = None
