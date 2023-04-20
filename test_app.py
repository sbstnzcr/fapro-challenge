import json
from datetime import date, timedelta
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_valid_date(client):
    valid_date = date.today().strftime("%Y-%m-%d")
    response = client.get(f"/api/uf?date={valid_date}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["date"] == valid_date
    assert isinstance(data["value"], float)


def test_invalid_date(client):
    invalid_date = "2023-13-01"
    response = client.get(f"/api/uf?date={invalid_date}")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data


def test_future_date(client):
    future_date = "2023-12-31"
    response = client.get(f"/api/uf?date={future_date}")
    assert response.status_code == 404
    data = json.loads(response.data)
    assert "error" in data


def test_missing_date(client):
    response = client.get("/api/uf")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
