# Define CRUD (Create, Read, Update, Delete) operations for interacting with the database.
# get_booking function retrieves a booking by its ID.
# create_booking function creates a new booking record in the database.


from sqlalchemy.orm import Session
import models, schemas

# Get a booking by ID
def get_booking(db: Session, booking_id: int):
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()

# Create a new booking
def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
