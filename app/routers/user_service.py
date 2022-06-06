from typing import List
from models.models import User
from models.schemas import user, auth_user
from fastapi import APIRouter
from dao.user import userDao
from dao.auth_user import AuthUserDao
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="USER_ROUTER")
from fastapi import Depends
from sqlalchemy.orm import Session
from .dependecies.database import DbConn 

user_router = APIRouter()

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@user_router.get("/token")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@user_router.get("/users", response_model=List[user.UserOut])
async def get_users(db: Session = Depends(DbConn.get_db)):
    return userDao.get_all_user(db, User)

## SQLAlchemy does not work on Async on current implementation
@user_router.post("/create/user", response_model=user.UserOut)
def create_user(user: user.UserModel, db: Session = Depends(DbConn.get_db)):
    custom_logger.info(user)
    custom_logger.info(db)
    # Check if the name already exists
    res = userDao.find_by_name(db, user.name)
    if res:
        custom_logger.warning("Already exists")
        return res
    else:
        return userDao.create_user(db, user)
    
@user_router.post("/create/auth_user", response_model=auth_user.AuthUserInDB)
def create_user(user: auth_user.AuthUserModelIn, db: Session = Depends(DbConn.get_db)):
    custom_logger.info(user)
    custom_logger.info(db)
    # Check if the name already exists
    # res = AuthUserDao.find_by_username(db, user.username)
    
    res=False
    if res:
        custom_logger.warning("Already exists")
        return res
    else:
        temp = AuthUserDao.create_auth_user(db, user)
        custom_logger.debug(temp)
        return temp