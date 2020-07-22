import logging

from fastapi import FastAPI

from app.api import ping, predictions
from app.db import database, engine, metadata


log = logging.getLogger(__name__)

metadata.create_all(engine)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(predictions.router, prefix="/predict", tags=["predict"])
    return application


app = create_application()


@app.on_event("startup")
async def startup():
    log.info("Starting up...")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    log.info("Shutting down...")
    await database.disconnect()
