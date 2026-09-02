from fastapi.testclient import TestClient
from src.main import app
from src.schemas.account import AccountCreate, AccountUpdate

client = TestClient(app)

def test_create_account():
    account_data = AccountCreate(account_number='123456789', balance=100.0, holder='John Doe', creation_date='2024-07-10')
    response = client.post('/accounts/', json=account_data.dict())
    assert response.status_code == 200
    assert response.json()['account_number'] == '123456789'

def test_read_account():
    response = client.get('/accounts/1')
    assert response.status_code == 200
    assert response.json()['account_number'] == '123456789'

def test_update_account():
    account_data = AccountUpdate(balance=200.0, holder='Jane Doe')
    response = client.put('/accounts/1', json=account_data.dict())
    assert response.status_code == 200
    assert response.json()['balance'] == 200.0

def test_delete_account():
    response = client.delete('/accounts/1')
    assert response.status_code == 200
    assert response.json()['detail'] == 'Account deleted'