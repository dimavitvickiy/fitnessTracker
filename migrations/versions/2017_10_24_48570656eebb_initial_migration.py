"""Initial migration

Revision ID: 48570656eebb
Revises: 
Create Date: 2017-10-24 17:08:46.955348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48570656eebb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('user')
