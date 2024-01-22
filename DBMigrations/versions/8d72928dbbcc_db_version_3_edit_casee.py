"""db version 3 edit casee

Revision ID: 8d72928dbbcc
Revises: a5000e28f9c8
Create Date: 2023-12-22 16:39:35.493433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d72928dbbcc'
down_revision: Union[str, None] = 'a5000e28f9c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cases', sa.Column('case_vertical', sa.String(length=60), nullable=False))
    op.drop_constraint('cases_case_vertical_id_fkey', 'cases', type_='foreignkey')
    op.drop_column('cases', 'case_vertical_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cases', sa.Column('case_vertical_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('cases_case_vertical_id_fkey', 'cases', 'verticals', ['case_vertical_id'], ['id'])
    op.drop_column('cases', 'case_vertical')
    # ### end Alembic commands ###
