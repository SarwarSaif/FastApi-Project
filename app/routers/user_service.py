from typing import List
# from app.models.schemas import user
from models.models import User
# from models.schemas.user import UserModel
from models.schemas import user
from dao.dao import Dao
from fastapi import APIRouter
from datetime import datetime

from dao.user import userDao

from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="ROUTER")



user_router = APIRouter()

@user_router.get("/users", response_model=List[user.UserModel])
async def get_users():
    return Dao().find_all(User)

@user_router.get("/create/user", response_model=user.CreateUserModel)
async def create_user(user: user.UserModel):
    custom_logger.info(user)
    db_user = User(
        name=user.name,
        is_active=True,
        date=datetime.now() #datetime.utcnow
        #hashed_password=hashed_password,
    )
    # t2 = Dao().user_insert(db_user)
    # custom_logger.debug("t2-> {}".format(t2))
    return Dao().user_insert(db_user)