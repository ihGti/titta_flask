"""empty message

Revision ID: 1d143e62db9a
Revises: 4c8cc8b7e03e
Create Date: 2023-12-14 17:11:23.593023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d143e62db9a'
down_revision = '4c8cc8b7e03e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__exhibit', schema=None) as batch_op:
        batch_op.drop_index('F_ExTitle')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__exhibit', schema=None) as batch_op:
        batch_op.create_index('F_ExTitle', ['F_ExTitle'], unique=False)

    # ### end Alembic commands ###