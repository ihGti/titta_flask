"""empty message

Revision ID: 7087ef3e145f
Revises: 67774c46c0d5
Create Date: 2023-11-21 21:28:32.718404

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7087ef3e145f'
down_revision = '67774c46c0d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__pet', schema=None) as batch_op:
        batch_op.alter_column('F_Size',
               existing_type=mysql.VARCHAR(length=256),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('F_Castration',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__pet', schema=None) as batch_op:
        batch_op.alter_column('F_Castration',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('F_Size',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###
