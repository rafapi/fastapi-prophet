from fastapi import FastAPI

from app.api import ping, predictions
from app.db import database, engine, metadata

metadata.create_all(engine)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
            predictions.router, prefix="/predict", tags=["predict"]
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
