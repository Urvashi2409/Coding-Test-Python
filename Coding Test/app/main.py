from fastapi import FastAPI
from app.api import auth, posts
from app.dependencies import get_current_user

app = FastAPI()

# Include authentication endpoints
app.include_router(auth.router)

# Include post-related endpoints
app.include_router(
    posts.router,
    prefix="/posts",
    tags=["posts"],
    dependencies=[Depends(get_current_user)]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
