import logging

from fastapi import FastAPI

from app.api import ping, predictions
from app.db import mk_engine, setup_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(predictions.router, prefix="/predict", tags=["predict"])
    return application


app = create_application()


@app.on_event("startup")
async def startup():
    log.info("Starting up...")
    mk_engine()
    # wait database.connect()


@app.on_event("shutdown")
async def shutdown():
    log.info("Shutting down...")
    database = setup_db()
    await database.disconnect()
