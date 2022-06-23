from fastapi import FastAPI
from db.db import Base, engine

from resources import meal, authentication



def create_app():
    Base.metadata.create_all(engine)
    app = FastAPI()
    app.include_router(meal.router)
    app.include_router(authentication.router)
    return app

app = create_app()
