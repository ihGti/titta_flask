"""empty message

Revision ID: 4e82135d4d4f
Revises: a1bf076c6d46
Create Date: 2023-11-11 21:03:28.580636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e82135d4d4f'
down_revision = 'a1bf076c6d46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__exhibit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('F_ExTime', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__exhibit', schema=None) as batch_op:
        batch_op.drop_column('F_ExTime')

    # ### end Alembic commands ###
