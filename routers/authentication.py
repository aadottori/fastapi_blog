import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from sqlalchemy.orm import Session
import models, schemas, database, hashing
from fastapi import APIRouter, HTTPException, status, Depends


router = APIRouter(
    prefix = "/authentication",
    tags = ["Authentication"]
)

@router.post("/")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials.")
    if not hashing.Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password.")
    #generate a jwt token and return it
    return user