"""empty message

Revision ID: 67774c46c0d5
Revises: b754d8432b0c
Create Date: 2023-11-20 22:29:25.673296

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '67774c46c0d5'
down_revision = 'b754d8432b0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__foster_pet',
    sa.Column('F_FosterPetID', sa.Integer(), nullable=False),
    sa.Column('F_FosterTitle', sa.String(length=256), nullable=False),
    sa.Column('F_Location', sa.String(length=256), nullable=False),
    sa.Column('F_FosterPlase', sa.String(length=256), nullable=False),
    sa.Column('F_Senoir', sa.String(length=256), nullable=False),
    sa.Column('F_Single', sa.String(length=256), nullable=False),
    sa.Column('F_FosterDate', sa.Date(), nullable=True),
    sa.Column('F_PetID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['F_PetID'], ['t__pet.F_PetID'], ),
    sa.PrimaryKeyConstraint('F_FosterPetID')
    )
    with op.batch_alter_table('t__pet', schema=None) as batch_op:
        batch_op.alter_column('F_Date',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('F_VeccineR',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('F_VeccineT',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__pet', schema=None) as batch_op:
        batch_op.alter_column('F_VeccineT',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('F_VeccineR',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('F_Date',
               existing_type=sa.DATE(),
               nullable=True)

    op.drop_table('t__foster_pet')
    # ### end Alembic commands ###
