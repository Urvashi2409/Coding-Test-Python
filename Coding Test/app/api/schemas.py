from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    Pydantic model for user creation request payload.
    """
    email: str
    password: str

class User(BaseModel):
    """
    Pydantic model for user response data.
    """
    id: int
    email: str

class PostCreate(BaseModel):
    """
    Pydantic model for post creation request payload.
    """
    text: str

class Post(BaseModel):
    """
    Pydantic model for post response data.
    """
    id: int
    text: str
    user_id: int
