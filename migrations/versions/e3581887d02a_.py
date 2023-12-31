"""empty message

Revision ID: e3581887d02a
Revises: ab73a4ac528e
Create Date: 2023-11-15 20:59:00.494641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3581887d02a'
down_revision = 'ab73a4ac528e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__pet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('F_UserID', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 't__user', ['F_UserID'], ['F_UserID'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__pet', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('F_UserID')

    # ### end Alembic commands ###
