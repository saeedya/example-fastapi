"""add content column to posts table

Revision ID: e96b4b58d37d
Revises: 91238fe137f9
Create Date: 2022-08-24 00:53:36.104256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e96b4b58d37d'
down_revision = '91238fe137f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
