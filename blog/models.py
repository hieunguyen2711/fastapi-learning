from .database import Base
from sqlalchemy import Column, String, Integer
class Blog(Base):
    __tablename__ = "blogs-db" #Create the SQLite table schemas.
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
