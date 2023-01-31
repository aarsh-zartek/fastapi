from typing import Optional
from fastapi import FastAPI, Path
from pydantic.main import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    pass_out: Optional[bool]


users = {
    1: {
        "name": "john doe",
        "age": 17,
    },
    2: {
        "name": "ram",
        "age": 15
    }
}

@app.get("/")
def index(value: bool=True):
    return {
        "hello": "world",
        "value": value
    }

@app.get("/stud/{id}")
def get_stud(id: int=Path(None, description="The ID of the student you want to view", gt=0)):
    return users[id]


@app.get("/student")
def get_by_name(name: str):
    for key, _ in users.items():
        if users[key]["name"] == name:
            return users[key]
    return {
        "data": "Not found"
    }

@app.post("/create")
def create(request: User):

    return {
        "data": f"created {request.name}"
    }
