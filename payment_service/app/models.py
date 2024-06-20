# Defines the Payment model using SQLAlchemy.
# Specifies the database table name and columns.

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    currency = Column(String, index=True)
    status = Column(String, index=True)
    method = Column(String, index=True)
