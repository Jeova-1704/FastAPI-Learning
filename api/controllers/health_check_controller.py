from fastapi import APIRouter
from ..contracts.health_check_response import HealthCheckResponse

router = APIRouter()


@router.get("", response_model=HealthCheckResponse)
async def health_check():
    return HealthCheckResponse(message="OK.")
