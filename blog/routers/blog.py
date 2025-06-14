from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, models
from typing import List

router = APIRouter()

#### Create a GET Method to Fetch all blogs from the DB ###### 
@router.get("/blog", response_model=List[schemas.ShowBlog], tags=['blogs'])
def get_all_blog(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return  blogs