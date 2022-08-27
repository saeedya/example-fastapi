"""create posts table

Revision ID: 91238fe137f9
Revises: 
Create Date: 2022-08-24 00:39:42.392671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91238fe137f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False)) 
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
