from pydantic import BaseModel, Field
from enum import Enum


class UserStatus(str, Enum):
    active = "Active"
    inactive = "Inactive"
    pending = "Pending"


class UserRole(str, Enum):
    master = "Master"
    admin = "Admin"
    agent = "Agent"


class UserVertical(str, Enum):
    payments = "Payments"
    procurement = "Procurement"
    platform = "Platform"
    sourcing = "Sourcing"


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
