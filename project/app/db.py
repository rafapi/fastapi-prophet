from databases import Database
from sqlalchemy import create_engine

from app.config import get_settings

settings = get_settings()


dburl = settings.database_url
if settings.testing:
    engine = create_engine(dburl, connect_args={"check_same_thread": False})
else:
    engine = create_engine(dburl)


dburl = settings.database_url
if settings.testing:
    database = Database(dburl, force_rollback=True)
else:
    database = Database(dburl)
