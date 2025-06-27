# Import BaseModel from pydantic for data validation and serialization
from pydantic import BaseModel
# Import List type hint for defining list fields
from typing import List

# Base schema for blog data - contains common fields for blog operations
class BlogBase(BaseModel):
    # Title field - required string for blog title
    title: str
    # Body field - required string for blog content
    body: str

    
# Complete blog schema that inherits from BlogBase
class Blog(BlogBase):
    # Configuration class for Pydantic model behavior
    class Config():
        # Enable automatic conversion from ORM objects (SQLAlchemy models)
        # This allows direct conversion from database models to Pydantic models
        from_attributes = True

# Schema for user data - used for user registration and updates
class User(BaseModel):
    # Name field - required string for user's name
    name: str
    # Email field - required string for user's email
    email: str
    # Password field - required string for user's password
    password: str


# Schema for displaying user information with their blogs
class ShowUser(BaseModel):
    # Name field - required string for user's name
    name: str
    # Email field - required string for user's email
    email: str
    # Blogs field - list of Blog objects associated with this user
    blogs: List[Blog]
    # Configuration class for Pydantic model behavior
    class Config():
        # Enable automatic conversion from ORM objects (SQLAlchemy models)
        from_attributes = True

# Schema for displaying blog information with creator details
class ShowBlog(BlogBase):
    # Title field - required string for blog title
    title: str
    # Body field - required string for blog content
    body: str
    # Creator field - ShowUser object representing the blog creator
    creator: ShowUser
    # Configuration class for Pydantic model behavior
    class Config():
        # Enable automatic conversion from ORM objects (SQLAlchemy models)
        from_attributes = True


# Schema for login requests
class Login(BaseModel):
    # Username field - required string for login username/email
    username: str
    # Password field - required string for login password
    password: str

# Schema for JWT token responses
class Token(BaseModel):
    # Access token field - string containing the JWT token
    access_token: str
    # Token type field - string indicating the token type (usually "bearer")
    token_type: str


# Schema for token data payload
class TokenData(BaseModel):
    # Email field - optional string for user email stored in token
    # Default value is None if not provided
    email: str | None = None
    