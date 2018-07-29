"""add initial_amount column

Revision ID: c82a79b74fde
Revises: 9082b5065144
Create Date: 2018-07-29 17:04:09.099034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c82a79b74fde'
down_revision = '9082b5065144'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('budget', sa.Column('intial_amount', sa.Float))


def downgrade():
    pass
