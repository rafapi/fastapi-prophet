from sqlalchemy import Column, Integer, String, DateTime, Table
from sqlalchemy.sql import func
from app.db import metadata


predictions = Table(
    "predictions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("ticker", String(6)),
    Column("prediction", String),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)
