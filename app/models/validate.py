from pydantic.types import conint, constr
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

#from .session import Base
from session import Base


from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator


from lib.mylogger import MyLogger
validation_logger = MyLogger(logger_name="VALIDATION")
#https://pydantic-docs.helpmanual.io/usage/types/#constrained-types
class ValidationModel(BaseModel):
    id: conint(gt=50, lt=100, multiple_of=5) #id: int # 
    count: int = Field(..., gt=50, lt=100, multiple_of=5) #Using the Field Function of pydantic
    name: constr(min_length=2, max_length=10) #id: str #strip_whitespace=True
    apple_based_food: constr(regex=r'^apple (pie|tart|sandwich)$')
    is_active: bool
    url: HttpUrl #HttpUrl Type object
    email_address:EmailStr #EmailStr Type object
    email_address_confirm:str #will use custom validators below
    password1:str #will use custom validators below
    password2:str #will use custom validators below
    
    #custom validators
    @validator('email_address_confirm')
    def email_address_match(cls, val, values, **kwargs): 
        if 'email_address' in values and val != values['email_address']:
            validation_logger.error('email addresses do not match')
            raise ValueError('email addresses do not match')
        return val
    
    @root_validator #Validation can also be performed on the entire model's data using @root_validator 
    def check_passwords_match(cls, values):
        # validation_logger.info(cls, values.get('password1'), values.get('password2'))
        # assert 'password1' not in values or 'password2' not in values, 'passwords must be provided'
        
        pw1, pw2 = values.get('password1'), values.get('password2')
        validation_logger.info(pw1, pw2)
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        
        # more attributes validations here
        
        return values
