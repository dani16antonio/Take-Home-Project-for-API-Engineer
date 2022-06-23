from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.db import get_db
from db.requests.login import get_token


router = APIRouter(prefix='/login', tags=['authentication'])

@router.post('/')
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    access_token = get_token(request, db)
    return {
        'access_token':access_token,
        'token_type':'bearer'
    }