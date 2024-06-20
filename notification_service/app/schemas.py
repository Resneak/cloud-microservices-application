# Defines Pydantic models for request and response validation.
# NotificationBase: Common fields for a notification.
# NotificationCreate: Schema for creating a new notification.
# Notification: Schema for reading a notification with an ID.
# Config class enables ORM mode for SQLAlchemy integration.

from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    message: str
    recipient: str
    timestamp: datetime

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int

    class Config:
        orm_mode = True
