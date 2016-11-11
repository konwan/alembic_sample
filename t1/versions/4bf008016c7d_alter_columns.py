"""alter columns

Revision ID: 4bf008016c7d
Revises: 698a3d124685
Create Date: 2016-11-11 23:19:29.320462

"""
from alembic import op
import sqlalchemy as sa

"""
Note “Batch mode” for SQLite and other databases is a new and intricate feature within the 0.7.0 series of Alembic,
and should be considered as “beta” for the next several releases.
"""
# revision identifiers, used by Alembic.
revision = '4bf008016c7d'
down_revision = '698a3d124685'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('telephone') as batch_op:
        batch_op.alter_column('telphone_no', new_column_name='phone', type_=sa.String(10),
                              existing_type=sa.String(10))
    # op.alter_column('telephone', 'telphone_no', new_column_name='phone',
    #                existing_type=sa.String(20))  existing_type=mysql.VARCHAR(length=20))


def downgrade():
    with op.batch_alter_table('telephone') as batch_op:
        batch_op.alter_column('phone', new_column_name='telphone_no', type_=sa.String(17),
                              existing_type=sa.String(length=17))
    # op.alter_column('telephone', 'phone', new_column_name='telphone_no',
    #                existing_type=sa.String(64))
