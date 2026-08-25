from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_get_quick_ratio_zero_liabilities():
    payload = {'cash': 20000, 'marketable_securities': 10000, 'receivables': 15000, 'current_liabilities': 0}
    response = client.post('/analytics/quick-ratio', json=payload)
    assert response.status_code == 400
