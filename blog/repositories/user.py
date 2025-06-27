# Import local modules for schemas and database models
from .. import schemas, models
# Import Session for database session management
from sqlalchemy.orm import Session
# Import Hash class for password hashing
from ..hashing import Hash
# Import FastAPI components for HTTP exception handling
from fastapi import HTTPException, status

# Function to create a new user in the database
def create(request: schemas.User, db: Session):
    # Create a new User model instance with hashed password
    # Hash.bcrypt() encrypts the plain text password before storing
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    # Add the new user to the database session
    db.add(new_user)
    # Commit the transaction to save the user to the database
    db.commit()
    # Refresh the user object to get any auto-generated values (like ID)
    db.refresh(new_user)
    # Return the created user object
    return new_user

# Function to fetch a single user by ID from the database
def fetchOne(id: int, db: Session):
    # Query the database to find user with the specified ID
    user = db.query(models.User).filter(models.User.id == id).first()
    # Check if user exists in the database
    if not user:
        # Raise HTTP 404 exception if user is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found!")
    # Return the found user object
    return user