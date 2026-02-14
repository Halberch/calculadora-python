import pytest
from calculadora.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_add(client):
    response = client.post('/add', json={'a': 10, 'b': 20})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 30

def test_api_subtract(client):
    response = client.post('/subtract', json={'a': 10, 'b': 4})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 6

def test_api_multiply(client):
    response = client.post('/multiply', json={'a': 5, 'b': 6})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 30

def test_api_divide(client):
    response = client.post('/divide', json={'a': 10, 'b': 2})
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 5

def test_api_divide_by_zero(client):
    response = client.post('/divide', json={'a': 20, 'b': 0})
    data = response.get_json()
    assert response.status_code == 400
    assert data['error'] == 'Invalid input for division.'
