# Import Session for database session management
from sqlalchemy.orm import Session
# Import local modules for database models and schemas
from .. import models
from .. import schemas
# Import FastAPI components for HTTP exception handling
from fastapi import HTTPException, status


# Function to retrieve all blogs from the database
def get_all(db: Session):
    # Query all Blog records from the database
    blogs = db.query(models.Blog).all()
    # Return the list of all blogs
    return  blogs

# Function to create a new blog in the database
def create(request: schemas.Blog, db: Session):
    # Create a new Blog model instance with the provided data
    # Note: user_id is hardcoded to 1 (should be current user's ID in production)
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    # Add the new blog to the database session
    db.add(new_blog)
    # Commit the transaction to save the blog to the database
    db.commit()
    # Refresh the blog object to get any auto-generated values (like ID)
    db.refresh(new_blog)
    # Return the created blog object
    return new_blog

# Function to delete a blog by ID from the database
def delete(id: int, db: Session):
    # Query the database to find blog with the specified ID
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # Check if blog exists in the database
    if not blog.first():
        # Raise HTTP 404 exception if blog is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found!")
    # Delete the blog from the database
    blog.delete(synchronize_session=False)
    # Commit the transaction to persist the deletion
    db.commit()
    # Return success message
    return 'Blog Deleted'

# Function to fetch a single blog by ID from the database
def fetch_one(id: int, db: Session):
    # Query the database to find blog with the specified ID
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # Check if blog exists in the database
    if not blog:
        # Raise HTTP 404 exception if blog is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found!")
    # Return the found blog object
    return blog

# Function to update a blog by ID in the database
def update(id: int, request: schemas.Blog, db: Session):
    # Query the database to find blog with the specified ID
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # Check if blog exists in the database
    if not blog.first():
        # Raise HTTP 404 exception if blog is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
    # Update the blog with new data from the request
    # model_dump() converts the Pydantic model to a dictionary
    blog.update(request.model_dump())
    # Commit the transaction to persist the changes
    db.commit()
    # Return success message
    return "Successfully Updated"