from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies import get_current_user
from app.api.schemas import PostCreate, Post
from app.services.post_service import PostService

router = APIRouter()

@router.post("/", response_model=Post)
def add_post(post_data: PostCreate, current_user: User = Depends(get_current_user)):
    """
    Endpoint for adding a new post.
    """
    post = PostService.create_post(post_data, current_user.id)
    return post

@router.get("/", response_model=list[Post])
def get_posts(current_user: User = Depends(get_current_user)):
    """
    Endpoint for fetching all posts of the current user.
    """
    posts = PostService.get_posts(current_user.id)
    return posts

@router.delete("/{post_id}")
def delete_post(post_id: int, current_user: User = Depends(get_current_user)):
    """
    Endpoint for deleting a post.
    """
    if not PostService.delete_post(post_id, current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return {"message": "Post deleted successfully"}
