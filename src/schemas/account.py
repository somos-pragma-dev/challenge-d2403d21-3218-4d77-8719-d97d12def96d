from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_number: str
    balance: float
    holder: str
    creation_date: str

class AccountUpdate(BaseModel):
    balance: float
    holder: str

class AccountResponse(BaseModel):
    id: int
    account_number: str
    balance: float
    holder: str
    creation_date: str