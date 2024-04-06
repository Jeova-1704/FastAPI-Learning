from pydantic import BaseModel, validator


class LoginRequest(BaseModel):
    email: str
    password: str

    @validator("email")
    def email_must_be_valid(cls, email: str) -> str:
        # TODO: implementar uma validação de email mais robusta
        if not "@" in email:
            raise ValueError("Invalid email")
        return email

    @validator("password")
    def password_must_be_valid(cls, password: str) -> str:
        # TODO: implementar uma validação de password mais robusta
        if len(password) < 8:
            raise ValueError("password must be at least 8 characters long")

        return password
