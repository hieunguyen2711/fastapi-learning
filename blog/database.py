# Import create_engine from SQLAlchemy to create database engine
from sqlalchemy import create_engine
# Import declarative_base to create base class for database models
from sqlalchemy.ext.declarative import declarative_base
# Import sessionmaker to create database session factory
from sqlalchemy.orm import sessionmaker

# Define the database URL for SQLite database
# This creates/connects to a file named 'blog.db' in the current directory
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db' #Connect to the blog database


######Create a connection to the SQLite database######
# Create a SQLAlchemy engine instance with SQLite database
# connect_args={"check_same_thread": False} allows multiple threads to use the same connection
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


#Creates a Factory for db session objects using SQLALchemy.
# SessionLocal is a factory that creates database session objects
# bind=engine: connects sessions to the database engine
# autoflush=False: disables automatic flushing of changes
# autocommit=False: disables automatic committing of transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False )

# Create a base class for all database models
# All models will inherit from this Base class
Base = declarative_base()

# Dependency function to get database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the calling function
        # This allows the session to be used in the endpoint
        yield db
    finally:
        # Always close the database session when done
        # This ensures proper cleanup of database connections
        db.close()