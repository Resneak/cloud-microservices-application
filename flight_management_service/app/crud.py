# Implements CRUD operations for the Flight model.
# get_flight: Retrieves a flight by ID.
# create_flight: Creates a new flight in the database.

from sqlalchemy.orm import Session
import models, schemas

def get_flight(db: Session, flight_id: int):
    return db.query(models.Flight).filter(models.Flight.id == flight_id).first()

def create_flight(db: Session, flight: schemas.FlightCreate):
    db_flight = models.Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

# function to remove a seat (via flight_number) after a user successfully books a seat using bookings/ POST
def decrement_seats(db: Session, flight_id: int):
    db_flight = get_flight(db, flight_id)
    if db_flight and db_flight.total_seats > 0:
        db_flight.total_seats -= 1
        db.commit()
        db.refresh(db_flight)
        return db_flight.total_seats
    else:
        raise Exception("No available seats or flight not found")
