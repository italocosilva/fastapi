from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_api_get_local_root():
    r = client.get('/')
    assert r.status_code != 200


def test_api_get_item_status():
    r = client.get('/items/12?count=20')
    assert r.status_code == 200


def test_api_get_item_response():
    r = client.get('/items/12?count=20')
    assert r.json()['fetch'] == 'Fetched 20 of 12'
