"""Initializaion AUTH 1.2

Revision ID: bdb9f0957f84
Revises: 3b6cbd78b962
Create Date: 2023-06-27 02:40:11.581780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdb9f0957f84'
down_revision = '3b6cbd78b962'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.drop_column('user', ' is_superuser')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column(' is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_superuser')
    # ### end Alembic commands ###