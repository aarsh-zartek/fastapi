from typing import List
from fastapi import APIRouter, BackgroundTasks, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.db import get_db
from app.oauth2 import get_user
from app.views import blog


router = APIRouter(prefix="/blog", tags=["Blogs"], dependencies=[Depends(get_user)])


@router.get("", response_model=List[schemas.DisplayBlog])
def all(
    db: Session = Depends(get_db),
    # get_current_user: schemas.User = Depends(get_user),
):
    return blog.list_all(db)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(bg_task: BackgroundTasks, request: schemas.Blog, db: Session = Depends(get_db)):
    return bg_task.add_task(blog.create, request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.DisplayBlog,
)
def retrieve(id, db: Session = Depends(get_db)):
    return blog.retrieve(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)
