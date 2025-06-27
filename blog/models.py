# Import Base class from database module to inherit from for SQLAlchemy models
from .database import Base
# Import SQLAlchemy column types and relationship functionality
from sqlalchemy import Column, String, Integer, ForeignKey
# Import relationship to define relationships between models
from sqlalchemy.orm import relationship 

# Define Blog model class that inherits from Base (SQLAlchemy declarative base)
class Blog(Base):
    # Specify the table name in the database
    __tablename__ = "blogs-db" #Create the SQLite table schemas.
    
    # Define id column as primary key with auto-increment and index
    id = Column(Integer, primary_key=True, index=True)
    # Define title column as string type for blog title
    title = Column(String)
    # Define body column as string type for blog content
    body = Column(String)
    # Define user_id column as foreign key referencing users.id
    user_id = Column(Integer, ForeignKey('users.id'))
    # Define relationship to User model - each blog has one creator (user)
    # back_populates="blogs" creates bidirectional relationship
    creator = relationship("User", back_populates="blogs")


    
# Define User model class that inherits from Base (SQLAlchemy declarative base)
class User(Base):
    # Specify the table name in the database
    __tablename__ = "users"
    
    # Define id column as primary key with auto-increment and index
    id = Column(Integer, primary_key=True, index=True)
    # Define name column as string type for user's name
    name = Column(String)
    # Define email column as string type for user's email
    email = Column(String)
    # Define password column as string type for user's password (should be hashed)
    password = Column(String)
    # Define relationship to Blog model - each user can have multiple blogs
    # back_populates="creator" creates bidirectional relationship
    blogs = relationship("Blog", back_populates="creator")


