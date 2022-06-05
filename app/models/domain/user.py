import email
from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional, Union
from datetime import date, datetime
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="DOMAIN")


class User(BaseModel):
    id: int
    name: str
    is_active: bool
    # date: Union[datetime, None] = None
    # custom_logger.info("User model got executed...")
    
    # class Config:
    #     orm_mode = True