from fastapi import FastAPI
from src.api.v1.account import account_router

app = FastAPI()

app.include_router(account_router)