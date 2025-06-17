from fastapi import FastAPI
from pydantic import BaseModel
from . import models
from .database import engine
from .routers import blog, user, auth


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)
@app.get('/')
def home():
    return {"testing": "Hello"}



class Blog(BaseModel):
    title: str
    body: str



