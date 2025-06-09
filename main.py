from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def start():
    return "Hello to my blog"

@app.get("/blog")
def index(limit=10, published:bool = True,sort:Optional[str] = None): #Assign the default value of the query params
    #Only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the db '}
    else:
        return {'data': f'{limit} blogs from the db '}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #Fetch comments of a single blog with id = id
    # return limit
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog/')
def create_blog(blog: Blog):
    # return blog
    return {'data': f"Blog is created successfully with title as {blog.title}"}

# if __name__  == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)