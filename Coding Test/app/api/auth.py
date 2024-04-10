from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies import oauth2_scheme
from app.services.user_service import UserService
from app.api.schemas import UserCreate, User
from app.utils import generate_token

router = APIRouter()

@router.post("/signup", response_model=User)
def signup(user_data: UserCreate):
    """
    Endpoint for user signup.
    """
    user = UserService.create_user(user_data)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return user

@router.post("/login", response_model=str)
def login(email: str, password: str):
    """
    Endpoint for user login.
    """
    user = UserService.authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = generate_token(email)
    return token
