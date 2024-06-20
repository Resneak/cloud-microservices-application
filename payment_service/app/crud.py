# Implements CRUD operations for the Payment model.
# get_payment: Retrieves a payment by ID.
# create_payment: Creates a new payment in the database.

from sqlalchemy.orm import Session
import models, schemas

def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit() # Commit the transaction to save changes
    db.refresh(db_payment)
    return db_payment
