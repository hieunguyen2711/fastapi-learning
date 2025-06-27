# Import FastAPI components for routing, dependencies, and status codes
from fastapi import APIRouter, Depends, status
# Import Session for database session management
from sqlalchemy.orm import Session
# Import local modules for schemas, database, and OAuth2 authentication
from .. import schemas, database, oauth2
# Import List type hint for response models
from typing import List
# Import blog repository for business logic operations
from ..repositories import blog

# Create an API router for blog endpoints with prefix and tag for organization
router = APIRouter(
        prefix="/blog",
        tags=['blogs']
    
    )

"""
    The code under is to perform the CRUD Operations for the Blogs.
"""

#### Create a GET Method to Fetch all blogs from the DB ###### 
# Define GET endpoint to retrieve all blogs with authentication required
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Call blog repository get_all method to fetch all blogs
    return blog.get_all(db)



 ####Create a POST Method to Insert a blog into the DB ######
# Define POST endpoint to create a new blog with authentication required
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Call blog repository create method to handle blog creation logic
    return blog.create(request, db)


##### Delete a single Blog from the DB ######
# Define DELETE endpoint to remove a blog by ID with authentication required
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_single(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Call blog repository delete method to remove the blog
    return blog.delete(id, db)

####Create a GET Method to Fetch one blog from the DB ######
# Define GET endpoint to retrieve a single blog by ID with authentication required
@router.get('/{id}',status_code=200, response_model=schemas.ShowBlog)
def fetch_one(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Call blog repository fetch_one method to get specific blog
    return blog.fetch_one(id, db)

##### Update the information of one blog #####
# Define PUT endpoint to update a blog by ID with authentication required
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Call blog repository update method to modify the blog
    return blog.update(id, request, db)
