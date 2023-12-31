"""empty message

Revision ID: de60ebb680bd
Revises: d509a6dd875a
Create Date: 2023-11-02 19:13:31.755720

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'de60ebb680bd'
down_revision = 'd509a6dd875a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__exhibit',
    sa.Column('F_ExID', sa.Integer(), nullable=False),
    sa.Column('F_ExTitle', sa.String(length=256), nullable=False),
    sa.Column('F_ExPrice', sa.Integer(), nullable=False),
    sa.Column('F_ExInfo', sa.String(length=256), nullable=False),
    sa.Column('F_ExPhoto', sa.String(length=256), nullable=False),
    sa.Column('F_UserID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['F_UserID'], ['t__user.F_UserID'], ),
    sa.PrimaryKeyConstraint('F_ExID'),
    sa.UniqueConstraint('F_ExTitle')
    )
    with op.batch_alter_table('t__user', schema=None) as batch_op:
        batch_op.alter_column('F_BirthDay',
               existing_type=mysql.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__user', schema=None) as batch_op:
        batch_op.alter_column('F_BirthDay',
               existing_type=mysql.DATETIME(),
               nullable=True)

    op.drop_table('t__exhibit')
    # ### end Alembic commands ###
