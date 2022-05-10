from typing import List, Union

from pydantic import BaseModel, AnyUrl, Field, validator


class CreateArchiveRequestSchema(BaseModel):
    urls: List[str] = Field(..., description="Upload URLs")


class CreateArchiveResponseSchema(BaseModel):
    archive_hash: str = Field(..., description="Download filename")


class ArchiveStatusWithURLResponseSchema(BaseModel):
    status: str = Field(..., description="Archive status")
    url: str = Field(..., description="Archived file URL")


class ArchiveStatusWithoutURLResponseSchema(BaseModel):
    status: str = Field(..., description="Archive status")


ArchiveStatusResponseSchema = Union[ArchiveStatusWithURLResponseSchema, ArchiveStatusWithoutURLResponseSchema]
