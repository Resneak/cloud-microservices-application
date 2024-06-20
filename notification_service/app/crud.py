# Implements CRUD operations for the Notification model.
# get_notification: Retrieves a notification by ID.
# create_notification: Creates a new notification in the database.

from sqlalchemy.orm import Session
import models, schemas

def get_notification(db: Session, notification_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notification_id).first()

def create_notification(db: Session, notification: schemas.NotificationCreate):
    db_notification = models.Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification
