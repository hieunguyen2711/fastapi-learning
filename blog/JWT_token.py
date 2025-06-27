# Import datetime classes for token expiration handling
from datetime import datetime, timedelta, timezone
# Import PyJWT library for JWT token creation and verification
import jwt
# Import schemas module for TokenData model
from . import schemas
# Import PyJWTError for exception handling
from jwt import PyJWTError



# Secret key used for signing and verifying JWT tokens
# In production, this should be stored in environment variables
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# Algorithm used for JWT token signing (HMAC with SHA-256)
ALGORITHM = "HS256"
# Token expiration time in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Function to create a new JWT access token
def create_access_token(data: dict):
    # Create a copy of the input data to avoid modifying the original
    to_encode = data.copy()
    # Calculate expiration time by adding minutes to current UTC time
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Add expiration timestamp to the token payload
    to_encode.update({"exp": expire})
    # Encode the data into a JWT token using the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # Return the encoded JWT token string
    return encoded_jwt

# Function to verify and decode a JWT token
def verify_token(token: str, credentials_exception):
    try: 
        # Decode the JWT token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extract the subject (email) from the token payload
        email = payload.get("sub")
        # Check if email exists in the token payload
        if email is None:
            # Raise credentials exception if email is missing
            raise credentials_exception
        # Create TokenData object with the extracted email
        token_data = schemas.TokenData(email=email)
    except PyJWTError:
        # Raise credentials exception if token is invalid or expired
        raise credentials_exception