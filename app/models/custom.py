from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional
from datetime import datetime
from models.user import UserModel
from models.parent import ParentModel

class CustomModel(BaseModel):
    name: str
    users: List[UserModel] = []
    parents: List[ParentModel] = []
    class Config:
        orm_mode = True
