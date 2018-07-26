"""Add user_id to Expense table

Revision ID: 9082b5065144
Revises: 
Create Date: 2018-07-25 21:22:33.267125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9082b5065144'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('expense', sa.Column('user_id', sa.Integer))


def downgrade():
    pass
