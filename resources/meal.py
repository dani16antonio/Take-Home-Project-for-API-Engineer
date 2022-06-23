from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from db.db import get_db
from db.requests.meal import get_all_meal



router = APIRouter(prefix='/menu', tags=['menu'])

@router.get('/{date}/{type_}')
def get_all_meals(date:str, type_:str, db:Session=Depends(get_db)):
    meal_names = get_all_meal(db, date, type_)
    if len(meal_names) < 1:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "There is not meal that match the criteria.")
    return [meal.name for meal in meal_names]
