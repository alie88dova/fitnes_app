"""DATABASE TEST 3

Revision ID: 7402a05175f0
Revises: a3d384c186c8
Create Date: 2023-06-26 23:59:39.529282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7402a05175f0'
down_revision = 'a3d384c186c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('passwords')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('passwords',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('usr_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['usr_id'], ['users.id'], name='passwords_usr_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='passwords_pkey')
    )
    # ### end Alembic commands ###
