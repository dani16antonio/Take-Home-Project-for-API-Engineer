from sqlalchemy import Column, ForeignKey, Integer
from db.db import  Base


class MealWeekDB(Base):
    __tablename__ = 'meal_week'
    meal_id = Column(Integer, ForeignKey('meal.id'), primary_key=True)
    week_id = Column(Integer, ForeignKey('week.id'), primary_key=True)
