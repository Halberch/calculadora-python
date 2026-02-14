import pytest
from calculadora.app import app


def _log_api_call(endpoint, payload, response):
    print(
        f"[integration] endpoint={endpoint} payload={payload} "
        f"status={response.status_code} body={response.get_json()}"
    )


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_add(client):
    payload = {'a': 10, 'b': 20}
    response = client.post('/add', json=payload)
    _log_api_call('/add', payload, response)
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 30

def test_api_subtract(client):
    payload = {'a': 10, 'b': 4}
    response = client.post('/subtract', json=payload)
    _log_api_call('/subtract', payload, response)
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 6

def test_api_multiply(client):
    payload = {'a': 5, 'b': 6}
    response = client.post('/multiply', json=payload)
    _log_api_call('/multiply', payload, response)
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 30

def test_api_divide(client):
    payload = {'a': 10, 'b': 2}
    response = client.post('/divide', json=payload)
    _log_api_call('/divide', payload, response)
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 5

def test_api_divide_by_zero(client):
    payload = {'a': 20, 'b': 0}
    response = client.post('/divide', json=payload)
    _log_api_call('/divide', payload, response)
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == 'Invalid input for division.'
