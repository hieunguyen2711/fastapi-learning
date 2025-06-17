from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, database, models
from typing import List

router = APIRouter()

#### Create a GET Method to Fetch all blogs from the DB ###### 
@router.get("/blog", response_model=List[schemas.ShowBlog], tags=['blogs'])
def get_all_blog(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return  blogs

 ####Create a POST Method to Insert a blog into the DB ######
@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

##### Delete a single Blog from the DB ######
@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete_single(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog Deleted'

####Create a GET Method to Fetch one blog from the DB ######
@router.get('/blog/{id}',status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def fetch_one(id,response : Response, db: Session = Depends(database.get_db), status_code=200):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found!")
    return blog

##### Update the information of one blog #####
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
    blog.update(request.model_dump())
    db.commit()
    return "Successfully Updated"
