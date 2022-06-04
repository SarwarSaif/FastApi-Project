#DTO to contain list of entities, but pydantis can handle the conversion of the entities to pydantis models

from models.models import CustomModel, Parent, User
from dao.dao import Dao
from fastapi import APIRouter

custom_service_router = APIRouter()

@custom_service_router.get("/custom", response_model=CustomModel)
async def get_custom_dtos_with_entities():
    users=Dao().find_all(User) 
    parents=Dao().find_all(Parent) 
    return CustomModel(name="John", users=users, parents=parents)