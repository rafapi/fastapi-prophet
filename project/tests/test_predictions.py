import json
import os
import pytest
from datetime import datetime

from app.api import crud
from app.config import get_settings
from app.utils import pred_to_dict


def test_db_test_url(test_app):
    settings = get_settings()
    assert settings.database_url == os.environ.get("DATABASE_TEST_URL")


@pytest.mark.asyncio
def test_create_prediction(test_app, db):
    test_request_payload = {"ticker": "GOOG"}

    response = test_app.post("/predict/", json.dumps(test_request_payload), db)

    prediction_id = response.json()["id"]

    assert response.status_code == 201
    assert response.json() == {"id": prediction_id, "ticker": "GOOG"}


def test_create_prediction_invalid_json(test_app):
    response = test_app.post("/predict/", data=json.dumps({2: "GOOG"}))
    assert response.status_code == 422


def test_read_prediction(test_app, db, monkeypatch):
    test_data = {
        "id": 1,
        "ticker": "MSFT",
        "prediction": json.dumps(
            {
                "07/22/2020": 212.29389088938012,
                "07/23/2020": 212.75441373941516,
                "07/24/2020": 213.21493658945016,
                "07/25/2020": 213.6754594394852,
                "07/26/2020": 214.1359822895202,
                "07/27/2020": 214.59650513955518,
                "07/28/2020": 215.05702798959027,
            }
        ),
        "created_date": datetime.utcnow().isoformat(),
    }

    async def mock_get(id, db):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/predict/1/")
    assert response.status_code == 200
    assert response.json() == pred_to_dict(test_data)


def test_read_prediction_incorrect_id(test_app, db):
    response = test_app.get("/predict/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Prediction not found"


@pytest.mark.asyncio
def test_delete_prediction(test_app, db):
    test_request_payload = {"ticker": "GOOG"}

    post_response = test_app.post(
        "/predict/", json.dumps(test_request_payload), db
    )
    prediction_id = post_response.json()["id"]

    del_response = test_app.delete(f"/predict/{prediction_id}/")

    assert del_response.json()["id"] == prediction_id
