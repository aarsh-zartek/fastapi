from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class User(BaseModel):

    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class DisplayUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class DisplayBlog(Blog):
    creator: ShowUser

    class Config:
        orm_mode = True



class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
