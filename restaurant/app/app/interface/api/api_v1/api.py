from fastapi import APIRouter

from app.interface.api.api_v1.endpoints import menu

api_router = APIRouter()

api_router.include_router(menu.router, prefix="/menus", tags=["menus"])
