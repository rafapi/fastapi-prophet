from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table
from sqlalchemy.sql import func

metadata = MetaData()

predictions = Table(
    "predictions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("ticker", String(6)),
    Column("prediction", String),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)
