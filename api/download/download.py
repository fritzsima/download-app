import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from core.fastapi.schemas.exception import ExceptionResponseSchema
from core.config import config

download_router = APIRouter()


@download_router.get(
    "/get/{filename}",
    responses={"400": {"model": ExceptionResponseSchema}}
)
def download_archive(filename):
    file_path = f'{config.STATIC_DIR}{filename}'
    if not os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="File not found")
    return FileResponse(file_path)
