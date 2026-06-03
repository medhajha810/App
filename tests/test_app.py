from app import app


def test_hello():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['message'] == 'Hello, world!'
from app import get_message


def test_get_message():
    assert get_message() == "Hello from App"