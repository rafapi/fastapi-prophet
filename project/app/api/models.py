from pydantic import BaseModel


class PredictionSchema(BaseModel):
    ticker: str
    description: str
