from pydantic import BaseModel


class StockIn(BaseModel):
    ticker: str


class StockOut(BaseModel):
    ticker: str
    prediction: str
