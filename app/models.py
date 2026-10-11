from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    fitness_goal = Column(String(50), nullable=False)
    experience_level = Column(String(30), nullable=False)
    food_preference = Column(String(30), nullable=False)

    plans = relationship(
        "FitnessPlan",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class FitnessPlan(Base):
    __tablename__ = "fitness_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    workout_plan = Column(String, nullable=False)
    meal_suggestions = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="plans")