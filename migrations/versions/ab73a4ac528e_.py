"""empty message

Revision ID: ab73a4ac528e
Revises: 998080452f39
Create Date: 2023-11-14 22:20:30.225376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab73a4ac528e'
down_revision = '998080452f39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__pet',
    sa.Column('F_PetID', sa.Integer(), nullable=False),
    sa.Column('F_Date', sa.Date(), nullable=True),
    sa.Column('F_VeccineR', sa.String(length=256), nullable=False),
    sa.Column('F_VeccineT', sa.String(length=256), nullable=False),
    sa.Column('F_Health', sa.String(length=256), nullable=False),
    sa.Column('F_Colors', sa.String(length=256), nullable=True),
    sa.Column('F_Seibetu', sa.String(length=256), nullable=False),
    sa.Column('F_Age', sa.Integer(), nullable=False),
    sa.Column('F_Size', sa.String(length=256), nullable=False),
    sa.Column('F_Castration', sa.String(length=256), nullable=True),
    sa.Column('F_Features', sa.String(length=256), nullable=False),
    sa.Column('F_Background', sa.String(length=256), nullable=False),
    sa.Column('F_Image', sa.String(length=256), nullable=False),
    sa.Column('F_Remarks', sa.String(length=256), nullable=False),
    sa.Column('F_CategoryID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['F_CategoryID'], ['t__category.F_CategoryID'], ),
    sa.PrimaryKeyConstraint('F_PetID')
    )
    with op.batch_alter_table('t__category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('F_CategoryCode', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__category', schema=None) as batch_op:
        batch_op.drop_column('F_CategoryCode')

    op.drop_table('t__pet')
    # ### end Alembic commands ###