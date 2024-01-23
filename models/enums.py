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


"""
Case defined enums
"""


class CaseStatus(str, Enum):
    open = "Open"
    closed_unresolved = "Closed Unresolved"
    closed_resolved = "Closed Resolved"
    escalated = "Escalated"
