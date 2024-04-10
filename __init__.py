from fastapi import FastAPI

app = FastAPI()

# Import routers and include them in the main app instance
from app.api import auth, posts

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
