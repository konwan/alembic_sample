"""add colunm to table

Revision ID: 20161115T18:31:44
Revises: 20161115T18:23:40
Create Date: 2016-11-15 18:31:44.686858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20161115T18:31:44'
down_revision = '20161115T18:23:40'
branch_labels = ()
depends_on = None


def upgrade():
    op.add_column('group', sa.Column('addgp', sa.String(length=100)))
    op.add_column('ta', sa.Column('addta', sa.String(length=100)))
    op.add_column('user', sa.Column('addus', sa.String(length=100)))


def downgrade():
    # op.drop_column('user', 'addus')
    # op.drop_column('ta', 'addta')
    # op.drop_column('group', 'addgp')
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('addus')
    with op.batch_alter_table('ta') as batch_op:
        batch_op.drop_column('addta')
    with op.batch_alter_table('group') as batch_op:
        batch_op.drop_column('addgp')
