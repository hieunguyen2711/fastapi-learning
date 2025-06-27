# Import FastAPI framework for creating web APIs
from fastapi import FastAPI
# Import BaseModel from pydantic for data validation and serialization
from pydantic import BaseModel
# Import models module from the current package for database models
from . import models
# Import engine from database module for database connection
from .database import engine
# Import router modules from routers package for organizing API endpoints
from .routers import blog, user, auth


# Create a FastAPI application instance
app = FastAPI()

# Create all database tables based on the models defined in models.py
# This ensures the database schema matches the SQLAlchemy models
models.Base.metadata.create_all(bind=engine)

# Include the blog router to handle blog-related endpoints
app.include_router(blog.router)
# Include the user router to handle user-related endpoints
app.include_router(user.router)
# Include the auth router to handle authentication-related endpoints
app.include_router(auth.router)

# Define a GET endpoint for the root path "/"
@app.get('/')
def home():
    # Return a simple test message when accessing the root URL
    return {"testing": "Hello"}



# Define a Pydantic model for blog data validation
class Blog(BaseModel):
    # Title field - required string for the blog title
    title: str
    # Body field - required string for the blog content
    body: str



