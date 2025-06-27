# Import FastAPI dependencies and HTTP exception handling
from fastapi import Depends, HTTPException, status
# Import Annotated for type annotations with metadata
from typing import Annotated
# Import JWT_token and schemas modules for token verification
from . import JWT_token, schemas
# Import OAuth2 security components for password bearer authentication
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Create OAuth2 password bearer scheme for token-based authentication
# tokenUrl="login" specifies the endpoint where clients can obtain tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dependency function to get the current authenticated user
def get_current_user(token: str = Depends(oauth2_scheme) ):
    # Create HTTP exception for invalid credentials
    # status_code=401: Unauthorized status code
    # detail: Error message explaining the issue
    # headers: Include WWW-Authenticate header for proper authentication flow
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # Verify the JWT token and return the token data (user information)
    # If token is invalid, the verify_token function will raise the credentials_exception
    return JWT_token.verify_token(token=token, credentials_exception=credentials_exception)
    