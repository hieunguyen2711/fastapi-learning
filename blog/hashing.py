from passlib.context import CryptContext


###### Hashing Class to endcrypt the password of users. ##########
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):   
        return pwd_context.hash(password)