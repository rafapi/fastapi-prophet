import logging

from fastapi import FastAPI

from app.api import ping, predictions, train
from app.db import get_eng, get_db
from app.models.sqlalchemy import metadata

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    app = FastAPI()
    app.include_router(ping.router)
    app.include_router(predictions.router, prefix="/predict", tags=["predict"])
    app.include_router(train.router, prefix="/train", tags=["train"])

    metadata.create_all(get_eng())
    database = get_db()

    @app.on_event("startup")
    async def startup():
        log.info("Starting up...")
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        log.info("Shutting down...")
        await database.disconnect()

    return app


app = create_application()
