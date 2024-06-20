# Defines Pydantic models for request and response validation.
# FlightBase: Common fields for a flight.
# FlightCreate: Schema for creating a new flight.
# Flight: Schema for reading a flight with an ID.
# Config class enables ORM mode for SQLAlchemy integration.

from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    flight_number: str
    departure: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    total_seats: int

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int

    class Config:
        from_attributes = True
