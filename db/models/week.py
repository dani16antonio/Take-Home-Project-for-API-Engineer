from sqlalchemy import Column, Date, Integer
from sqlalchemy.orm import relationship
from db.db import Base



class WeekDB(Base):
    __tablename__ = 'week'
    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    
    meals = relationship('MealDB', secondary='meal_week', back_populates='dates', foreign_keys=('[MealWeekDB.meal_id, MealWeekDB.week_id]'))
