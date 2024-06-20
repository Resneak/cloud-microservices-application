# Define the database connection URL.
# Create an engine to manage the database connection.
# Create a sessionmaker for database sessions.
# Define a base class for declarative models.
# Define the Booking model representing the bookings table.


from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import Base

# Database connection URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create an engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Booking model
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    flight_number = Column(String, index=True)
    seat_number = Column(String, index=True)
    flight_id = Column(Integer, index=True)
    booking_time = Column(DateTime, index=True)  # Adding booking_time field
