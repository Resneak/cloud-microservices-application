# Initialize the FastAPI application.
# Create the database tables.
# Define the API endpoints for creating and retrieving payments.

import crud, models, schemas, database
from database import engine
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Endpoint to create a payment
@app.post("/payments/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(database.get_db)):
    return crud.create_payment(db=db, payment=payment)

# Endpoint to read a payment by ID
@app.get("/payments/{payment_id}", response_model=schemas.Payment)
def read_payment(payment_id: int, db: Session = Depends(database.get_db)):
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment
