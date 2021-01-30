from databases import Database
from sqlalchemy import create_engine, MetaData
from app.config import get_settings


settings = get_settings()
DATABASE_URL = settings.database_url

# create database schema
metadata = MetaData()


def get_engine():
    # create engine to communicate with the database
    return create_engine(DATABASE_URL)


# databases query builder
database = Database(DATABASE_URL)
