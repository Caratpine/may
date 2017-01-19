"""add Reminder

Revision ID: d1e1a418ba4
Revises: None
Create Date: 2017-01-19 22:12:48.028997

"""

# revision identifiers, used by Alembic.
revision = 'd1e1a418ba4'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('B')
    op.drop_table('A')
    op.drop_table('C')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('C',
    sa.Column('msg', mysql.TEXT(), nullable=True),
    sa.Column('time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('level', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('A',
    sa.Column('msg', mysql.TEXT(), nullable=True),
    sa.Column('time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('level', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('B',
    sa.Column('msg', mysql.TEXT(), nullable=True),
    sa.Column('time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('level', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('reminder')
    ### end Alembic commands ###