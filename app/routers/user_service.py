from typing import List
# from app.models.schemas import user
from models.models import User
# from models.schemas.user import UserModel
from models.schemas import user
from dao.dao import Dao
from fastapi import APIRouter

from dao.user import userDao

from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="ROUTER")

from fastapi import Depends
from sqlalchemy.orm import Session
from models.database import SessionLocal
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user_router = APIRouter()

@user_router.get("/users", response_model=List[user.UserModel])
async def get_users():
    return Dao().find_all(User)

@user_router.post("/create/user", response_model=user.CreateUserModel)
async def create_user(user: user.UserModel, db: Session = Depends(get_db)):
    custom_logger.info(user)
    
    try:
        t2 = Dao.create_user(db, user)
        custom_logger.debug("Service t2-> {}".format(t2))
    except Exception as err:
        custom_logger.error(err)
    return t2