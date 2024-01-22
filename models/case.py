import sqlalchemy
from db import metadata
from models.enums import CaseStatus

"""
cases: Table contains structure for cases
"""
case = sqlalchemy.Table(
    "cases",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("case_vertical", sqlalchemy.String(60), nullable=False),
    sqlalchemy.Column("case_topic", sqlalchemy.String(60), nullable=False),
    sqlalchemy.Column("case_status", sqlalchemy.Enum(CaseStatus), nullable=False, server_default=CaseStatus.open.name),
    sqlalchemy.Column("creation_date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("solution_score", sqlalchemy.Float, nullable=False, server_default="0.0"),
    sqlalchemy.Column("description", sqlalchemy.Text, nullable=True),
    sqlalchemy.Column("resources", sqlalchemy.Text, nullable=True),
    sqlalchemy.Column("salesforce_case_number", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("jira_escalation_number", sqlalchemy.Integer, nullable=True),
)
