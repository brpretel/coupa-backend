"""create db

Revision ID: 46c0c717b952
Revises: 
Create Date: 2024-01-22 19:26:55.951584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46c0c717b952'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('user_vertical', sa.String(length=30), nullable=False),
    sa.Column('status', sa.Enum('active', 'inactive', 'pending', name='userstatus'), server_default='pending', nullable=False),
    sa.Column('user_role', sa.Enum('master', 'admin', 'agent', name='userrole'), server_default='agent', nullable=False),
    sa.Column('creation_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('verticals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vertical_name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('case_vertical', sa.String(length=60), nullable=False),
    sa.Column('case_topic', sa.String(length=60), nullable=False),
    sa.Column('case_status', sa.Enum('open', 'closed_unresolved', 'closed_resolved', 'escalated', name='casestatus'), server_default='open', nullable=False),
    sa.Column('creation_date', sa.Date(), nullable=False),
    sa.Column('solution_score', sa.Float(), server_default='0.0', nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('resources', sa.Text(), nullable=True),
    sa.Column('salesforce_case_number', sa.Integer(), nullable=False),
    sa.Column('jira_escalation_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cases')
    op.drop_table('verticals')
    op.drop_table('users')
    # ### end Alembic commands ###