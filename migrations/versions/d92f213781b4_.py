"""empty message

Revision ID: d92f213781b4
Revises: 7714600bcbeb
Create Date: 2023-11-14 17:43:58.178512

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd92f213781b4'
down_revision = '7714600bcbeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('T_Login',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('point_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['point_id'], ['t__point.F_PointID'], ),
    sa.ForeignKeyConstraint(['user_id'], ['t__user.F_UserID'], ),
    sa.PrimaryKeyConstraint('user_id', 'point_id')
    )
    op.drop_table('t_login')
    with op.batch_alter_table('t__user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('points', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t__user', schema=None) as batch_op:
        batch_op.drop_column('points')

    op.create_table('t_login',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('point_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['point_id'], ['t__point.F_PointID'], name='t_login_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['t__user.F_UserID'], name='t_login_ibfk_2'),
    sa.PrimaryKeyConstraint('user_id', 'point_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('T_Login')
    # ### end Alembic commands ###