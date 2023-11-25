"""empty message

Revision ID: 85fd9a37228c
Revises: 7087ef3e145f
Create Date: 2023-11-21 22:06:47.869900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85fd9a37228c'
down_revision = '7087ef3e145f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__foster_pet', schema=None) as batch_op:
        batch_op.alter_column('F_FosterDate',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__foster_pet', schema=None) as batch_op:
        batch_op.alter_column('F_FosterDate',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=True)

    # ### end Alembic commands ###
