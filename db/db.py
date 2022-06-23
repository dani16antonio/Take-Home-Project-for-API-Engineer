from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.settings import Settings

@lru_cache()
def get_settings():
    return Settings()



# SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{get_settings().DATABASE_USER}:{get_settings().DATABASE_PASSWORD}@{get_settings().DATABASE_HOST}:{get_settings().DATABASE_PORT}/{get_settings().DATABASE_SCHEMA}'
SQLALCHEMY_DATABASE_URL = 'sqlite:///./db.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session_local = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()
 