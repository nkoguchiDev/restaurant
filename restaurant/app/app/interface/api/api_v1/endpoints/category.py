from fastapi import APIRouter
from pydantic import BaseModel, UUID4
from typing import List


router = APIRouter()


class Category(BaseModel):
    id: UUID4
    name: str
    description: str


class Categories(BaseModel):
    menus: List[Category]


@router.get("/", response_model=Categories)
def get_categories():
    return
