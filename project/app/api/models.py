from datetime import datetime
from pydantic import BaseModel


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    id: int


class PredictionSchema(StockOut):
    prediction: str
    created_date: datetime
