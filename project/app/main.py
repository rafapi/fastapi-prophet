from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .model import convert, predict
from app.api import ping
from app.db import engine, metadata, database


metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)


# pydantic models
class StockIn(BaseModel):
    ticker: str


class StockOut(BaseModel):
    forecast: dict


@app.post("/predict", response_model=StockOut, status_code=200)
async def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = await predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}

    return response_object
