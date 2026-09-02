from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud.account import create_account, get_account, update_account, delete_account
from src.schemas.account import AccountCreate, AccountUpdate, AccountResponse
from src.config.database import get_db

account_router = APIRouter()

@account_router.post('/accounts/', response_model=AccountResponse)
def create_account_endpoint(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)

@account_router.get('/accounts/{account_id}', response_model=AccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = get_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@account_router.put('/accounts/{account_id}', response_model=AccountResponse)
def update_account_endpoint(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = update_account(db, account_id, account)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@account_router.delete('/accounts/{account_id}')
def delete_account_endpoint(account_id: int, db: Session = Depends(get_db)):
    delete_account(db, account_id)
    return {'detail': 'Account deleted'}