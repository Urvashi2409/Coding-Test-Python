from fastapi import APIRouter

router = APIRouter()

from . import auth, posts
