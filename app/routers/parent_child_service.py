from typing import List
from models.models import Parent, ParentModel
from dao.dao import Dao
from fastapi import APIRouter


parent_router = APIRouter()

@parent_router.get("/parents", response_model=List[ParentModel])
async def get_parents():
    return Dao().find_all(Parent) #orm_mode = True in the model so that you can return an entity and pydantic will map it to the api models
                                  # In this case "Parent" Entity is return and pydantic has auto-mapped it to the "ParentModel" in the json response