from pydantic import BaseModel, Field
from models.enums import UserStatus, UserRole


class UserRegistrationData(BaseModel):
    username: str
    password: str
    user_vertical: str
    status: UserStatus = Field(default=UserStatus.pending)
    user_role: UserRole = Field(default=UserRole.agent)


class UserLoginData(BaseModel):
    username: str
    password: str