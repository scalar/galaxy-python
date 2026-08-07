# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PlanetUploadImageResponse"]


class PlanetUploadImageResponse(BaseModel):
    message: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """The URL where the uploaded image can be accessed"""

    uploaded_at: Optional[datetime] = FieldInfo(alias="uploadedAt", default=None)
    """Timestamp when the image was uploaded"""

    file_size: Optional[int] = FieldInfo(alias="fileSize", default=None)
    """Size of the uploaded image in bytes"""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """The content type of the uploaded image"""
