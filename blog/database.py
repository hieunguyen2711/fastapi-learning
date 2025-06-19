from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db' #Connect to the blog database


######Create a connection to the SQLite database######
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


#Creates a Factory for db session objects using SQLALchemy.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False )
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()