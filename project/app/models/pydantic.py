from datetime import datetime

from pydantic import BaseModel


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    id: int


class PredictionSchema(StockOut):
    prediction: dict
    created_date: datetime

    class Config:
        orm_mode = True
