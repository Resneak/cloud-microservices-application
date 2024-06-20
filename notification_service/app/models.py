# Defines the Notification model using SQLAlchemy.
# Specifies the database table name and columns.

from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    recipient = Column(String, index=True)
    timestamp = Column(DateTime, index=True)
