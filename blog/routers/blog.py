from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from typing import List
from ..repositories import blog

router = APIRouter(
        prefix="/blog",
        tags=['blogs']
    
    )

"""
    The code under is to perform the CRUD Operations for the Blogs.
"""

#### Create a GET Method to Fetch all blogs from the DB ###### 
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)



 ####Create a POST Method to Insert a blog into the DB ######
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


##### Delete a single Blog from the DB ######
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_single(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)

####Create a GET Method to Fetch one blog from the DB ######
@router.get('/{id}',status_code=200, response_model=schemas.ShowBlog)
def fetch_one(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.fetch_one(id, db)

##### Update the information of one blog #####
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
