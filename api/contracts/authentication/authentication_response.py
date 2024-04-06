from pydantic import BaseModel


class AuthenticationResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    token: str
