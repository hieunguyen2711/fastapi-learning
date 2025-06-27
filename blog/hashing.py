# Import CryptContext from passlib for password hashing and verification
from passlib.context import CryptContext


###### Hashing Class to endcrypt the password of users. ##########
# Create a password hashing context using bcrypt algorithm
# schemes=["bcrypt"]: specifies bcrypt as the hashing algorithm
# deprecated="auto": automatically handles deprecated hash formats
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash class containing methods for password hashing and verification
class Hash():
    # Static method to hash a plain text password using bcrypt
    def bcrypt(password: str):   
        # Hash the password using the bcrypt algorithm and return the hashed string
        return pwd_context.hash(password)
    
    # Static method to verify a plain text password against a hashed password
    def verify(hashed_password, plain_password):
        # Compare the plain text password with the hashed password
        # Returns True if they match, False otherwise
        return pwd_context.verify(plain_password, hashed_password)