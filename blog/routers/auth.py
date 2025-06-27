# Import FastAPI components for routing, dependencies, and HTTP exceptions
from fastapi import APIRouter, Depends, HTTPException, status
# Import local modules for schemas, database, models, and JWT functionality
from .. import schemas, database, models, JWT_token
# Import Hash class for password verification
from ..hashing import Hash
# Import Session for database session management
from sqlalchemy.orm import Session
# Import OAuth2PasswordRequestForm for login form handling
from fastapi.security import OAuth2PasswordRequestForm

# Create an API router for authentication endpoints with tag for API documentation
router = APIRouter(tags=["Authentication"])

# Define POST endpoint for user login
@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    # Query the database to find user by email (username field in OAuth2 form)
    user = db.query(models.User).filter(models.User.email == request.username).first()
    # Check if user exists in the database
    if not user:
        # Raise HTTP 404 exception if user is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {request.username} not found!")
    # Verify the provided password against the stored hashed password
    if not Hash.verify(user.password, request.password):
        # Raise HTTP 404 exception if password is incorrect
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    ##Generate a JWT Token if password is correct
    # Create JWT access token with user email as subject
    access_token = JWT_token.create_access_token(data={"sub": user.email})
    # Return the access token and token type in the response
    return {"access_token":access_token, "token_type": "bearer"}
    