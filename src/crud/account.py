from sqlalchemy.orm import Session
from src.models.account import Account
from src.schemas.account import AccountCreate, AccountUpdate, AccountResponse

def create_account(db: Session, account: AccountCreate) -> AccountResponse:
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return AccountResponse.from_orm(db_account)

def get_account(db: Session, account_id: int) -> AccountResponse:
    return db.query(Account).filter(Account.id == account_id).first()

def update_account(db: Session, account_id: int, account: AccountUpdate) -> AccountResponse:
    db_account = db.query(Account).filter(Account.id == account_id).first()
    for key, value in account.dict().items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return AccountResponse.from_orm(db_account)

def delete_account(db: Session, account_id: int):
    db.query(Account).filter(Account.id == account_id).delete()
    db.commit()