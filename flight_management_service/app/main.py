# Initialize the FastAPI application.
# Create the database tables.
# Define the API endpoints for creating and retrieving flights.

import crud, models, schemas, database
from database import engine
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import requests

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Endpoint to create a flight
@app.post("/flights/", response_model=schemas.Flight)
def create_flight(flight: schemas.FlightCreate, db: Session = Depends(database.get_db)):
    return crud.create_flight(db=db, flight=flight)

# Endpoint to read a flight by ID
@app.get("/flights/{flight_id}", response_model=schemas.Flight)
def read_flight(flight_id: int, db: Session = Depends(database.get_db)):
    db_flight = crud.get_flight(db, flight_id=flight_id)
    if db_flight is None:
        raise HTTPException(status_code=404, detail="Flight not found")
    return db_flight


