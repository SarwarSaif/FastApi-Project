from typing import List
from models.models import User, UserModel
from dao import Dao
from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/users", response_model=List[UserModel])
async def get_users():
    return Dao().find_all(User)

@user_router.get("/create/user")
async def create_user(user: UserModel):
    print(user)