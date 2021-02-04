import os
from databases import Database
from sqlalchemy import create_engine

# from app.config import get_settings

# settings = get_settings()


dburl = os.getenv("DATABASE_URL")
if os.getenv("TESTING"):
    engine = create_engine(dburl, connect_args={"check_same_thread": False})
    database = Database(dburl, force_rollback=True)
else:
    engine = create_engine(dburl)
    database = Database(dburl)
