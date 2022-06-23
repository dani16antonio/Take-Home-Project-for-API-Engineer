from sqlalchemy import and_
from sqlalchemy.orm import Session
from db.models.week import WeekDB
from db.models.meal import MealDB
from db.models.mealweek import MealWeekDB


def get_all_meal(db:Session, date:str, type_:str):
    return db.query(MealDB.name)\
        .filter(MealDB.type==type_)\
        .filter(and_(WeekDB.start_date<=date, WeekDB.end_date>=date))\
        .filter(MealWeekDB.meal_id==MealDB.id, MealWeekDB.week_id==WeekDB.id)\
        .all()
