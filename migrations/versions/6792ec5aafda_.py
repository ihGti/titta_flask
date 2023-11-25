"""empty message

Revision ID: 6792ec5aafda
Revises: d50f0a30f1bb
Create Date: 2023-11-22 21:48:42.418457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6792ec5aafda'
down_revision = 'd50f0a30f1bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__chat',
    sa.Column('F_ChatID', sa.Integer(), nullable=False),
    sa.Column('F_SenderID', sa.Integer(), nullable=False),
    sa.Column('F_ReceiverID', sa.Integer(), nullable=False),
    sa.Column('F_ChatContest', sa.String(length=256), nullable=False),
    sa.Column('F_ChatTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['F_ReceiverID'], ['t__user.F_UserID'], ),
    sa.ForeignKeyConstraint(['F_SenderID'], ['t__user.F_UserID'], ),
    sa.PrimaryKeyConstraint('F_ChatID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t__chat')
    # ### end Alembic commands ###
