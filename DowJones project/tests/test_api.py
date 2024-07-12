import sys
import os

path_to_projectroot = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path_to_projectroot)
from fastapi.testclient import TestClient
from api.app import app
import json


client = TestClient(app)


TICKERS = ["AAPL", "MSFT", "AXP"]

for ticker in TICKERS:

    def test_predict_endpoint_for_ticker():
        response = client.post("/api/predict/", json={"ticker": ticker, "days": 5})
        assert response.status_code == 200
        data = response.json()
        assert "predictions" in data
        assert "mse" in data


def test_predict_endpoint_days_exceed():
    response = client.post("/api/predict/", json={"ticker": "AAPL", "days": 9999})
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Le nombre de jours demandés dépassent les données de test disponibles"
    )
