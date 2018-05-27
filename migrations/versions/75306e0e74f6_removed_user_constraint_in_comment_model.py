"""removed user constraint in Comment model 

Revision ID: 75306e0e74f6
Revises: 419ff0dbbaf3
Create Date: 2018-05-27 07:37:51.774250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75306e0e74f6'
down_revision = '419ff0dbbaf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###