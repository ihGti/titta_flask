"""empty message

Revision ID: 7ebdfc4e1cf0
Revises: 85fd9a37228c
Create Date: 2023-11-22 17:22:21.257528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ebdfc4e1cf0'
down_revision = '85fd9a37228c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__lost_pet',
    sa.Column('F_LostPetID', sa.Integer(), nullable=False),
    sa.Column('F_LostTitle', sa.String(length=256), nullable=False),
    sa.Column('F_LostDate', sa.Date(), nullable=False),
    sa.Column('F_LostPlase', sa.String(length=256), nullable=False),
    sa.Column('F_LostInjury', sa.String(length=256), nullable=False),
    sa.Column('F_LostInstitution', sa.String(length=256), nullable=False),
    sa.Column('F_LostPlace', sa.String(length=256), nullable=False),
    sa.Column('F_LostFeatures', sa.String(length=256), nullable=False),
    sa.Column('F_LostLocation', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('F_LostPetID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t__lost_pet')
    # ### end Alembic commands ###
