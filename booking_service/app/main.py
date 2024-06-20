# Initialize the FastAPI application.
# Create and manage database tables.
# Define endpoints for the booking service.


import crud, models, schemas, database
from database import engine
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import requests
from fastapi import HTTPException

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# interact with the Flight Management Service
def get_flight_details(flight_id: int):
    response = requests.get(f"http://flight_management_service:80/flights/{flight_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Flight not found")
    
# function that removes available seats (via flight_number) by -1 once user has a confirmed booking (via bookings/ POST request)
def decrement_flight_seats(flight_details):
    if flight_details["total_seats"] > 0:
        flight_details["total_seats"] -= 1
        return flight_details["total_seats"]
    else:
        raise HTTPException(status_code=400, detail="No seats available")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Booking Service"} # returns message to user when user hits homepage

# Create a new booking and decrement available seats by -1 (include in response json)
@app.post("/bookings/", response_model=schemas.BookingResponse)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(database.get_db)):
    try:
        flight_details = get_flight_details(booking.flight_id)
        remaining_seats = decrement_flight_seats(flight_details)
        created_booking = crud.create_booking(db=db, booking=booking)
        return {
            "id": created_booking.id,
            "customer_name": created_booking.customer_name,
            "flight_number": created_booking.flight_number,
            "seat_number": created_booking.seat_number,
            "flight_id": created_booking.flight_id,
            "booking_time": created_booking.booking_time,
            "remaining_seats": remaining_seats
        }
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        raise HTTPException(status_code=500, detail="Internal Server Error")





# Read a booking by ID
@app.get("/bookings/{booking_id}", response_model=schemas.BookingBase)
def read_booking(booking_id: int, db: Session = Depends(database.get_db)):
    db_booking = crud.get_booking(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking



