from fastapi import FastAPI

from .models import Base
from .db import engine
from .routers import auth, blog, user

tags_metadata = [
    {
        "name": "Blogs",
        "description": "Manage Blogs. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
    {
        "name": "Users",
        "description": "Operations with users. The **login** logic is also here.",
    },
]

app = FastAPI(
    title="Hello, FastAPI",
    description="My first FastAPI blog app",
    version="0.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Black Virus",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)
