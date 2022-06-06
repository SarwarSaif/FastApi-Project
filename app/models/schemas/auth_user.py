import email
from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional, Union
from datetime import date, datetime
from lib.mylogger import MyLogger
custom_logger = MyLogger(logger_name="SCHEMA")
from models.domain.user import User

##### Authenticated User #######
class AuthUserModelIn(BaseModel):
    # id: int
    username: str
    email_address:EmailStr #EmailStr Type object
    email_address_confirm:str #will use custom validators below
    password1:str #will use custom validators below
    password2:str #will use custom validators below
    first_name: str
    last_name: str
    is_active: bool
    # is_superuser: bool
    # date: Union[datetime, None] = None
    #custom validators
    @validator('email_address_confirm')
    def email_address_match(cls, val, values, **kwargs): 
        if 'email_address' in values and val != values['email_address']:
            custom_logger.warning('email addresses do not match')
            raise ValueError('email addresses do not match')
        return val
    @root_validator #Validation can also be performed on the entire model's data using @root_validator 
    def check_passwords_match(cls, values):
        # validation_logger.info(cls, values.get('password1'), values.get('password2'))
        assert 'password1' in values or 'password2' in values, 'passwords must be provided'
        
        pw1, pw2 = values.get('password1'), values.get('password2')
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            custom_logger.warning('passwords do not match')
            raise ValueError('passwords do not match')
        return values



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