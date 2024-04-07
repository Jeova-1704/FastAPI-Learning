from fastapi import APIRouter
from .health_check_controller import router as health_check_router
from .authentication.authentication_controller import router as authentication_router

main_router = APIRouter()

main_router.include_router(
    health_check_router, prefix="/health_check", tags=["health_check"]
)


main_router.include_router(
    authentication_router, prefix="/authentication", tags=["authentication"]
)
