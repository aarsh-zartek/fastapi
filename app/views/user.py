from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.utils import Hash


def create(request: schemas.User, db: Session):

    user = models.User(
        name=request.name, email=request.email, password=Hash.encrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def retrieve(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user
