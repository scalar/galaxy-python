# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PlanetListAllDataParams"]


class PlanetListAllDataParams(TypedDict, total=False):

    limit: int
    """The number of items to return"""

    offset: int
    """The number of items to skip before starting to collect the result set"""
