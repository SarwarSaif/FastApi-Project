from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional
from datetime import datetime
from .child import ChildModel
       
class ParentModel(BaseModel):
    #id: int
    #parent_id: int
    email: str
    first_name: str
    last_name: str
    children: List[ChildModel] = []
    class Config:
        orm_mode = True
