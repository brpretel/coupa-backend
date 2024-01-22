import sqlalchemy
from db import metadata

"""
varticals: Table contains structure for user verticals
"""
vertical = sqlalchemy.Table(
    "verticals",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("vertical_name", sqlalchemy.String(60), nullable=False),
)
