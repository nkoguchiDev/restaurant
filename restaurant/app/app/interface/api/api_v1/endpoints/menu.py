from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, UUID4
from typing import List


router = APIRouter()


class CreatedMenu(BaseModel):
    name: str
    description: str
    price: int
    categoryId: UUID4
    imageUrl: HttpUrl


class Menu(CreatedMenu):
    id: UUID4


class MenuList(BaseModel):
    menus: List[Menu]


@router.get("/", response_model=MenuList)
def get_menus():
    return


@router.post("/", response_model=Menu)
def create_menu(menu: CreatedMenu):
    return
