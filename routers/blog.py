import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 


from fastapi import APIRouter, Depends, HTTPException, status
import schemas, database
from typing import List
from sqlalchemy.orm import Session
from repository import blog

router = APIRouter(
    prefix = "/blog",
    tags = ["Blogs"]
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all_blogs(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create_blog(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_single_blog(id, db: Session = Depends(get_db)):
    return blog.get_single_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED) 
def update_single_blog(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_single_blog(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_blog(id, db: Session = Depends(get_db)):
    return blog.delete_single_blog(id, db)


