from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional
from datetime import datetime
from .user import UserModel
from .parent import ParentModel

class CustomModel(BaseModel):
    name: str
    users: List[UserModel] = []
    parents: List[ParentModel] = []
    class Config:
        orm_mode = True
