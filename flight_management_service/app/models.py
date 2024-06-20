# Defines the Flight model using SQLAlchemy.
# Specifies the database table name and columns.

from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, index=True)
    departure = Column(String, index=True)
    destination = Column(String, index=True)
    departure_time = Column(DateTime, index=True)
    arrival_time = Column(DateTime, index=True)
    total_seats = Column(Integer, index=True)
