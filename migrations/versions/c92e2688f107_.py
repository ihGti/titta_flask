"""empty message

Revision ID: c92e2688f107
Revises: 03f7a89a0cfe
Create Date: 2023-11-23 22:31:50.143582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c92e2688f107'
down_revision = '03f7a89a0cfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__user_review',
    sa.Column('F_UserReviewID', sa.Integer(), nullable=False),
    sa.Column('F_ReviewID', sa.Integer(), nullable=False),
    sa.Column('F_ReviewFollowID', sa.Integer(), nullable=False),
    sa.Column('F_UserReviewMessage', sa.String(length=256), nullable=False),
    sa.Column('F_Score', sa.Integer(), nullable=False),
    sa.Column('F_Thumnbs', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['F_ReviewFollowID'], ['t__user.F_UserID'], ),
    sa.ForeignKeyConstraint(['F_ReviewID'], ['t__user.F_UserID'], ),
    sa.PrimaryKeyConstraint('F_UserReviewID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t__user_review')
    # ### end Alembic commands ###
