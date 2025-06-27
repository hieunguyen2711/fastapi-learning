# Import FastAPI components for routing, dependencies, and status codes
from fastapi import APIRouter, Depends, status
# Import Session for database session management
from sqlalchemy.orm import Session
# Import local modules for schemas and database functionality
from .. import schemas, database
# Import user repository for business logic operations
from ..repositories import user


"""
    The code under is to perform CRUD Operations for Users
"""

# Create an API router for user endpoints with tag and prefix for organization
router = APIRouter(tags=['users'], prefix="/user")
# Get database dependency function for dependency injection
get_db = database.get_db

##### Create a POST method to create a new user.
# Define POST endpoint for user creation with 201 status code and response model
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # Call user repository create method to handle user creation logic
    return user.create(request, db)


# Define GET endpoint to fetch a single user by ID with response model
@router.get('/{id}', response_model=schemas.ShowUser)
def fetchOneUser(id: int, db: Session = Depends(get_db)):
    # Call user repository fetchOne method to get user by ID
    return user.fetchOne(id, db)