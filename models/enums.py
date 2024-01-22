from builtins import str
from enum import Enum

"""
User defined enums
"""


class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    pending = "pending"


class UserRole(str, Enum):
    master = "master"
    admin = "admin"
    agent = "agent"


class CaseStatus(str, Enum):
    open = "open"
    closed_unresolved = "closed_unresolved"
    closed_resolved = "closed_resolved"
    escalated = "escalated"
