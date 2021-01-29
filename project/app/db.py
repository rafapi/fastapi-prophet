import os

from databases import Database
from sqlalchemy import create_engine, MetaData


# create database schema
metadata = MetaData()


def get_engine():
    # create engine to communicate with the database
    return create_engine(os.getenv("DATABASE_URL"))


# databases query builder
database = Database(os.getenv("DATABASE_URL"))
