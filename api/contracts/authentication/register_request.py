from pydantic import BaseModel, validator


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    @validator("first_name")
    def first_name_must_be_valid(cls, first_name: str) -> str:
        if len(first_name) < 2 or len(first_name) > 15:
            raise ValueError("First name must be between 2 and 15 characters long")
        return first_name

    @validator("last_name")
    def last_name_must_be_valid(cls, last_name: str) -> str:
        if len(last_name) < 2 or len(last_name) > 15:
            raise ValueError("Last name must be between 2 and 15 characters long")
        return last_name

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
