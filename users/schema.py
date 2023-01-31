from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    # name: str
    age: int
    admin: Optional[bool]
