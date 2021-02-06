import os

import asyncio
import pytest
from fastapi.testclient import TestClient

from app.config import get_settings

from app.db import database
from app.main import create_application


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
def test_app():
    settings = get_settings()
    if settings.database_url is None:
        settings.testing = True
        settings.environment = "test"
        settings.database_url = os.getenv("DATABASE_TEST_URL")
    app = create_application()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="module")
async def db():
    await database.connect()
    yield
    await database.disconnect()
