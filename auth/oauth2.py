from datetime import datetime, timedelta
import fastapi


from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from utils.settings import get_settings
from jose import jwt



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict, expire_delta:Optional[timedelta]=None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    enconded_jwt = jwt.encode(to_encode, get_settings().SECRET_KEY, algorithm=ALGORITHM)
    return enconded_jwt
