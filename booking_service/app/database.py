# Set up the database connection and provide a session to interact with the database.
# Create the SQLAlchemy engine to manage the database connection.
# Create a configured session factory to produce session objects.
# Define a dependency function to provide and close database sessions.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # disabled autoflush

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
