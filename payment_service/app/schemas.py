# Defines Pydantic models for request and response validation.
# PaymentBase: Common fields for a payment.
# PaymentCreate: Schema for creating a new payment.
# Payment: Schema for reading a payment with an ID.
# Config class enables ORM mode for SQLAlchemy integration.

from pydantic import BaseModel

class PaymentBase(BaseModel):
    amount: float
    currency: str
    status: str
    method: str

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True # enables automatic conversion
