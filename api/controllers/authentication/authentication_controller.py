from fastapi import APIRouter, status
from ...contracts.authentication.login_request import LoginRequest
from ...contracts.authentication.authentication_response import AuthenticationResponse
from ...contracts.authentication.register_request import RegisterRequest

router = APIRouter()


@router.post(
    "/login", status_code=status.HTTP_200_OK, response_model=AuthenticationResponse
)
def login(request_body: LoginRequest):
    return AuthenticationResponse(
        id=0,
        first_name="Not implemented yet",
        last_name="Not implemented yet",
        email=request_body.email,
        token="Not implemented yet",
    )

@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=AuthenticationResponse
)
def register(request_body: RegisterRequest):
    return AuthenticationResponse(
        id=0,
        first_name=request_body.first_name,
        last_name=request_body.last_name,
        email=request_body.email,
        token="Not implemented yet",
    )
