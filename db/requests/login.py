from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils.hash import Hash
from auth import oauth2


def get_token(request:OAuth2PasswordRequestForm, db:Session):
    dummy_user = 'danicrack'
    dummy_password = Hash.bcrypt('bigpass')
    if request.username == dummy_user and Hash.verify(dummy_password, request.password):
        return oauth2.create_access_token(data={'sub':request.username})
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user or password wrong.")
    
