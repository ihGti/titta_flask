"""empty message

Revision ID: bad5b6b6da13
Revises: fc0d609dddab
Create Date: 2024-01-11 17:36:56.640052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bad5b6b6da13'
down_revision = 'fc0d609dddab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__exhibit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('F_Sold', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__exhibit', schema=None) as batch_op:
        batch_op.drop_column('F_Sold')

    # ### end Alembic commands ###