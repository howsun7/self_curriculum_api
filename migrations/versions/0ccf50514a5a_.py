"""empty message

Revision ID: 0ccf50514a5a
Revises: b7d3c0774085
Create Date: 2022-06-08 19:52:38.667203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ccf50514a5a'
down_revision = 'b7d3c0774085'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curriculums', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.drop_constraint('curriculums_creater_id_fkey', 'curriculums', type_='foreignkey')
    op.create_foreign_key(None, 'curriculums', 'users', ['creator_id'], ['id'])
    op.drop_column('curriculums', 'creater_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curriculums', sa.Column('creater_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'curriculums', type_='foreignkey')
    op.create_foreign_key('curriculums_creater_id_fkey', 'curriculums', 'users', ['creater_id'], ['id'])
    op.drop_column('curriculums', 'creator_id')
    # ### end Alembic commands ###
