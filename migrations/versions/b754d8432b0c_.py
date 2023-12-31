"""empty message

Revision ID: b754d8432b0c
Revises: e3581887d02a
Create Date: 2023-11-17 22:51:46.862911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b754d8432b0c'
down_revision = 'e3581887d02a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__cartlist',
    sa.Column('F_CartID', sa.Integer(), nullable=False),
    sa.Column('F_UserID', sa.Integer(), nullable=False),
    sa.Column('F_ExID', sa.Integer(), nullable=False),
    sa.Column('F_CartPrice', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['F_ExID'], ['t__exhibit.F_ExID'], ),
    sa.ForeignKeyConstraint(['F_UserID'], ['t__user.F_UserID'], ),
    sa.PrimaryKeyConstraint('F_CartID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t__cartlist')
    # ### end Alembic commands ###
