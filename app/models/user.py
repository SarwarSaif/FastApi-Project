import email
from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional, Union
from datetime import date, datetime
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="SCHEMA")
from models.domain.user import User

## Schemas for User ###
class UserInLogin(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class UserInCreate(UserInLogin):
    username: str

class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None

class UserWithToken(User):
    token: str

class UserInResponse(BaseModel):
    user: UserWithToken
    class Config:
        orm_mode = True

class UserOut(User):
    date: Union[datetime, None] = None
    
    # custom_logger.info("User model got executed...")
    class Config:
        orm_mode = True

class UserIn(User):
    # custom_logger.info("User model got executed...")
    class Config:
        orm_mode = True

class UserModel(BaseModel):
    id: int
    name: str
    is_active: bool
    # date: Union[datetime, None] = None
    # custom_logger.info("User model got executed...")
    
    class Config:
        orm_mode = True
# class CreateUserModel(BaseModel):
#     id: int
#     name: str
#     is_active: bool
#     date: Union[datetime, None] = None
    
#     # custom_logger.info("User model got executed...")
#     class Config:
#         orm_mode = True
    
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")    
def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user