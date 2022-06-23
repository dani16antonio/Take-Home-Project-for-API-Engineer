from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base


class MealDB(Base):
    __tablename__ = 'meal'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    dates = relationship('WeekDB', secondary='meal_week', back_populates='meals', foreign_keys=('[MealWeekDB.meal_id, MealWeekDB.week_id]'))