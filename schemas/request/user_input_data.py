from pydantic import BaseModel, Field
from enum import Enum


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"


class UserRole(str, Enum):
    master = "master"
    admin = "admin"
    agent = "agent"


class UserVertical(str, Enum):
    payments = "payments"
    procurement = "procurement"
    platform = "platform"
    sourcing = "sourcing"


"""
User Request Schemas
"""


# User Registration Schema
class UserRegistrationData(BaseModel):
    username: str
    password: str
    user_vertical: UserVertical
    status: UserStatus = Field(default=UserStatus.pending)
    user_role: UserRole = Field(default=UserRole.agent)


# User Login Schema
class UserLoginData(BaseModel):
    username: str
    password: str
