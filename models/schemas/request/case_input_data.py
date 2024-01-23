from pydantic import BaseModel
from models.enums import CaseStatus


class CaseCreateRequest(BaseModel):
    case_type: str
    case_status: CaseStatus
    description: str
    resources: str
    salesforce_case_number: int
    jira_escalation_number: int
