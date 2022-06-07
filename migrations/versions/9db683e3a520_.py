"""empty message

Revision ID: 9db683e3a520
Revises: e4e10698fba3
Create Date: 2022-06-07 13:31:53.853855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9db683e3a520'
down_revision = 'e4e10698fba3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.Integer(), nullable=False, autoincrement=True))
    op.drop_column('users', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('users', 'id')
    # ### end Alembic commands ###
