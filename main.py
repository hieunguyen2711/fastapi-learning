# Import FastAPI framework for creating web APIs
from fastapi import FastAPI
# Import Optional type hint for optional parameters
from typing import Optional
# Import BaseModel from pydantic for data validation and serialization
from pydantic import BaseModel
# Import uvicorn ASGI server for running the FastAPI application
import uvicorn

# Create a FastAPI application instance
app = FastAPI()

# Define a GET endpoint for the root path "/"
@app.get("/")
def start():
    # Return a simple welcome message when accessing the root URL
    return "Hello to my blog"

# Define a GET endpoint for "/blog" with query parameters
@app.get("/blog")
def index(limit=10, published:bool = True,sort:Optional[str] = None): #Assign the default value of the query params
    # Check if only published blogs are requested
    if published:
        # Return a message indicating published blogs with the specified limit
        return {'data': f'{limit} published blogs from the db '}
    else:
        # Return a message indicating all blogs (published and unpublished) with the specified limit
        return {'data': f'{limit} blogs from the db '}


# Define a GET endpoint for "/blog/unpublished" to get unpublished blogs
@app.get('/blog/unpublished')
def unpublished():
    # Return a message indicating all unpublished blogs
    return {'data': 'all unpublished blogs'}


# Define a GET endpoint for "/blog/{id}" with path parameter
@app.get('/blog/{id}')
def show(id:int):
    # Return the blog ID as data (this would typically fetch blog details from database)
    return {'data': id}



# Define a GET endpoint for "/blog/{id}/comments" with path and query parameters
@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #Fetch comments of a single blog with id = id
    # return limit
    # Return a set of comment IDs (this would typically fetch actual comments from database)
    return {'data': {'1', '2'}}

# Define a Pydantic model for blog data validation
class Blog(BaseModel):
    # Title field - required string
    title: str
    # Body field - required string
    body: str
    # Published field - optional boolean (can be None)
    published: Optional[bool]


# Define a POST endpoint for "/blog/" to create new blogs
@app.post('/blog/')
def create_blog(blog: Blog):
    # return blog
    # Return a success message with the created blog's title
    return {'data': f"Blog is created successfully with title as {blog.title}"}

# Commented out code for running the server directly
# if __name__  == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)