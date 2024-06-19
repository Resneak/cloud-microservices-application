# Define Pydantic models for request and response validation.
# BookingCreate schema validates data for creating a new booking.
# Booking schema validates and serializes data for returning booking information.
# Config with orm_mode = True enables compatibility with ORMs.


from pydantic import BaseModel

# Schema for creating a booking
class BookingCreate(BaseModel):
    customer_name: str
    flight_number: str
    seat_number: str

# Schema for returning booking information
class Booking(BookingCreate): #inherits from the booking create schema
    id: int

    class Config:
        orm_mode = True
