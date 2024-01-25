from pydantic import BaseModel
from enum import Enum


class CaseStatus(str, Enum):
    open = "Open"
    closed_unresolved = "Closed Unresolved"
    closed_resolved = "Closed Resolved"
    escalated = "Escalated"


# Create Case Schema
class CaseCreateRequest(BaseModel):
    case_type: str
    case_status: CaseStatus
    description: str
    resources: str
    salesforce_case_number: int
    jira_escalation_number: int
