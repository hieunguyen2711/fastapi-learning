from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repositories import user


"""
    The code under is to perform CRUD Operations for Users
"""

router = APIRouter(tags=['users'], prefix="/user")
get_db = database.get_db

##### Create a POST method to create a new user.
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def fetchOneUser(id: int, db: Session = Depends(get_db)):
    return user.fetchOne(id, db)