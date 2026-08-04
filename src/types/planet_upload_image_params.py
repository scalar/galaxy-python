# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict
from .._types import FileTypes

__all__ = ["PlanetUploadImageParams"]


class PlanetUploadImageParams(TypedDict, total=False):

    image: FileTypes
    """The image file to upload"""
