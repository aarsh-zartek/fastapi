from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base


class Blog(Base):

    __tablename__ = "Blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)

    creator = relationship("User", back_populates="blogs",)


class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
