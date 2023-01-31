from sqlalchemy import Boolean, Column, Integer, String
from .db import Base

class User(Base):

    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    # name = Column(String)
    age = Column(Integer)
    admin = Column(Boolean)
