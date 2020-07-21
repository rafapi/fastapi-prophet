import os

import pytest
from starlette.testclient import TestClient

from app.main import create_application
from app.config import Settings, get_settings


def get_settings_override():
    return Settings(testing=1, ddatabase_url=os.environ.get("DATABASE_URL_TEST"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_override[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client
