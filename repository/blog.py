import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status



def get_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(
                        title=request.title, 
                        body=request.body, 
                        user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show_single_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not available.")
    return blog


def delete_single_blog(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not available.")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


def update_single_blog(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not available.")
    blog.update(request.dict()) 
    db.commit() 
    return "Update"
