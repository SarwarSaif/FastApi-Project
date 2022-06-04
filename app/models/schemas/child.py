from pydantic import BaseModel, HttpUrl, Field, EmailStr, validator, root_validator
from typing import List, Optional
from datetime import datetime

class ChildModel(BaseModel):
    #id: int
    #parent_id: int
    child_name: str
    date: datetime
    class Config:
        orm_mode = True
   