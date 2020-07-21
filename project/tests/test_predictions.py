import json
from datetime import datetime

import pytest

from app.api import crud, predictions
from app.utils import pred_to_dict


def test_create_prediction(test_app, monkeypatch):
    test_request_payload = {"ticker": "GOOG"}
    test_response_payload = {"id": 1, "ticker": "GOOG"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    def mock_generate_prediction(id, ticker):
        return None
    monkeypatch.setattr(predictions, "generate_prediction", mock_generate_prediction)

    response = test_app.post("/predict/",
                             data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_prediction_invalid_json(test_app):
    response = test_app.post("/predict/", data=json.dumps({2: "GOOG"}))
    assert response.status_code == 422


def test_read_prediction(test_app, monkeypatch):
    test_data = {
            "id": 1,
            "ticker": "TEST",
            "prediction": json.dumps({
                "07/22/2020": 212.29389088938012,
                "07/23/2020": 212.75441373941516,
                "07/24/2020": 213.21493658945016,
                "07/25/2020": 213.6754594394852,
                "07/26/2020": 214.1359822895202,
                "07/27/2020": 214.59650513955518,
                "07/28/2020": 215.05702798959027
            }),
            "created_date": datetime.utcnow().isoformat()
    }

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/predict/1/")
    assert response.status_code == 200
    assert response.json() == pred_to_dict(test_data)


def test_read_prediction_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/predict/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Prediction not found"
