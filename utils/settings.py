import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_USER:str
    DATABASE_PASSWORD:str
    DATABASE_HOST:str
    DATABASE_PORT:int
    DATABASE_SCHEMA:str
    
    class Config:
        env_file = '.env'
