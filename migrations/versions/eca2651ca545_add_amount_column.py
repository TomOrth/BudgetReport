"""Add amount column

Revision ID: eca2651ca545
Revises: 
Create Date: 2018-07-14 21:31:17.218303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca2651ca545'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('budget', sa.Column('amount', sa.Integer))


def downgrade():
    pass
