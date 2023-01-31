from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas


def list_all(db: Session) -> list:
    return db.query(models.Blog).all()


def create(request: schemas.Blog, db: Session):
    instance = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def retrieve(id: int, db: Session):
    instance = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return instance


def update(id: int, request: schemas.Blog, db: Session) -> dict:
    instance = db.query(models.Blog).filter(models.Blog.id == id)
    if not instance.filter():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    instance.update(
        {"title": request.title, "body": request.body}, synchronize_session=False
    )
    db.commit()
    return {"data": instance}


def delete(id: int, db: Session) -> None:
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.filter():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    blog.delete(synchronize_session=False)
    db.commit()
    return None
