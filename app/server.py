from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core.fastapi.dependencies import Logging
from api.archive import archive_router
from api.download import download_router


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(archive_router, prefix="/api/archive")
    app.include_router(download_router, prefix='/archive')


def init_listeners(app: FastAPI) -> None:
    pass


def init_middleware(app: FastAPI) -> None:
    pass


def init_cache(app: FastAPI) -> None:
    pass


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None,
        redoc_url=None,
        dependencies=[Depends(Logging)],
    )
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    init_middleware(app=app)
    init_cache(app=app)
    return app


app = create_app()
