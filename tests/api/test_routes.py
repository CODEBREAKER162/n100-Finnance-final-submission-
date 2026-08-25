import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_debt_to_equity_valid():
    response = client.post("/analytics/debt-to-equity", json={"total_debt": 50000, "total_equity": 100000})
    assert response.status_code == 200
    assert response.json() == {"ratio": 0.5}

def test_get_debt_to_equity_zero_equity():
    response = client.post("/analytics/debt-to-equity", json={"total_debt": 50000, "total_equity": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Total equity cannot be zero."

def test_get_quick_ratio_valid():
    payload = {
        "cash": 20000,
        "marketable_securities": 10000,
        "receivables": 15000,
        "current_liabilities": 30000
    }
    response = client.post("/analytics/quick-ratio", json=payload)
    assert response.status_code == 200
    assert response.json() == {"ratio": 1.5}
