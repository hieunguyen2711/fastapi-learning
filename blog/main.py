from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic import BaseModel
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Blog(BaseModel):
    title: str
    body: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

 ####Create a POST Method to Insert into the DB ######
@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

##### Delete a single Blog from the DB ######
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_single(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found!")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog Deleted'

##### Update the information of one blog #####
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")
    blog.update(request.model_dump())
    db.commit()
    return "Successfully Updated"


#### Create a GET Method to Fetch all from the DB ###### 
@app.get("/blog", response_model=List[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return  blogs

####Create a GET Method to Fetch one from the DB ######
@app.get('/blog/{id}',status_code=200, response_model=schemas.ShowBlog)
def fetch_one(id,response : Response, db: Session = Depends(get_db), status_code=200):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Not Found!")
    return blog