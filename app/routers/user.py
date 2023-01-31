from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.views import user

router = APIRouter(prefix="/user", tags=["Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.DisplayUser,
)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get(
    "/{id}",
    response_model=schemas.DisplayUser,
)
def retrieve_user(id, db: Session = Depends(get_db)):
    return user.retrieve()
