"""create tables

Revision ID: 42fcf016f047
Revises: 3a64d1e35c2e
Create Date: 2023-03-16 08:00:17.119722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42fcf016f047'
down_revision = '3a64d1e35c2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('preview', sa.String(), nullable=True),
    sa.Column('minutes_to_read', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('articles')
    # ### end Alembic commands ###
