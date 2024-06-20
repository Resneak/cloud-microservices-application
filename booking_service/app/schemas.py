# Define Pydantic models for request and response validation.
# BookingCreate schema validates data for creating a new booking.
# BookingBase schema validates and serializes data for returning booking information.
# BookingResponse schema extends BookingBase to include remaining_seats.
# Config with from_attributes = True enables compatibility with ORMs.

from pydantic import BaseModel
from datetime import datetime

# Schema for creating a booking
class BookingCreate(BaseModel):
    customer_name: str
    flight_number: str
    seat_number: str
    flight_id: int
    booking_time: datetime

# Base schema for returning booking information
class BookingBase(BookingCreate):
    id: int

    class Config:
        from_attributes = True

# Schema for returning booking information with remaining seats
class BookingResponse(BookingBase):
    remaining_seats: int  # Adding remaining_seats field
