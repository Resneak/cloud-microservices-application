# Initialize the FastAPI application.
# Create the database tables.
# Define the API endpoints for creating and retrieving notifications.

import crud, models, schemas, database
from database import engine
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Endpoint to create a notification
@app.post("/notifications/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(database.get_db)):
    return crud.create_notification(db=db, notification=notification)

# Endpoint to read a notification by ID
@app.get("/notifications/{notification_id}", response_model=schemas.Notification)
def read_notification(notification_id: int, db: Session = Depends(database.get_db)):
    db_notification = crud.get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification
