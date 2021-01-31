import logging

from fastapi import FastAPI

from app.api import ping, predictions
from app.db import metadata, mk_engine, setup_db


log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        predictions.router, prefix="/predict", tags=["predict"]
    )
    return application


app = create_application()
engine = mk_engine()
database = setup_db()


def create_schema():
    metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    log.info("Starting up...")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    log.info("Shutting down...")
    await database.disconnect()
