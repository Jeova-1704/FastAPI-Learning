from fastapi import APIRouter
from .health_check_controller import router as health_check_router

main_router = APIRouter()

main_router.include_router(health_check_router, prefix="/health_check", tags=["health_check"])
