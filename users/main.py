from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from users.db import SessionLocal, engine
from . import models, schema

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/post")
def create(request: schema.User, db: Session=Depends(get_db)):
    new_user = models.User(
        username=request.username,
        # name=request.name,
        age=request.age,
        admin=request.admin
    )

    db.add(new_user)
    db.commit()
    db.refresh()
    return new_user
