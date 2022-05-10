import uuid
from core.config import config
from fastapi import APIRouter, BackgroundTasks
from os.path import exists


from app.archive.schemas.archive import (
    CreateArchiveRequestSchema,
    CreateArchiveResponseSchema,
    ArchiveStatusResponseSchema
)
from core.fastapi.schemas.exception import ExceptionResponseSchema
from app.archive.services import archive_urls

archive_router = APIRouter()


@archive_router.post(
    "/create",
    response_model=CreateArchiveResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}}
)
def create_archive(request: CreateArchiveRequestSchema, background_tasks: BackgroundTasks):
    filename = str(uuid.uuid4())
    background_tasks.add_task(archive_urls, **request.dict(), filename=filename)
    # fileurl = f'http://{config.APP_HOST}:{config.APP_PORT}/archive/get/{filename}'
    return {"archive_hash": filename}


@archive_router.get(
    "/status/{filename}",
    response_model=ArchiveStatusResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}}
)
def get_archive_status(filename):
    archived_file = f'{config.STATIC_DIR}{filename}.zip'
    if exists(archived_file):
        archived_url = f'{config.BASE_URL}/archive/get/{filename}.zip'
        return {"status": "completed", "url": archived_url}
    else:
        return {"status": "in-progress"}
