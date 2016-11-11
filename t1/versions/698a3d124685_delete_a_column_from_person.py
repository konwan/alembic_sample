"""delete a column from person

Revision ID: 698a3d124685
Revises: 3715f217a003
Create Date: 2016-11-11 17:06:20.881246

"""
from alembic import op, context
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from ctest import Person
from sqlalchemy.orm import sessionmaker

# revision identifiers, used by Alembic.
revision = '698a3d124685'
down_revision = '3715f217a003'
branch_labels = None
depends_on = None


def upgrade():
    # sqlite not support  op.drop_column('person', 'idcard')
    op.create_table('person_bk',
                    sa.Column('person_id', sa.Integer, primary_key=True),
                    sa.Column('nickname', sa.String(64), nullable=False),
                    sa.Column('gender', sa.Integer),
                    sa.Column('idcard', sa.String(20))
                    )

    person_table = table('person_bk',
                         column('person_id', sa.Integer),
                         column('nickname', sa.String(64)),
                         column('gender', sa.Integer),
                         column('idcard', sa.String(20))
                         )

    url = context.config.get_main_option("sqlalchemy.url")
    engine = sa.create_engine(url)
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    data = [{'person_id': man.person_id,
             'nickname': man.nickname,
             'gender': man.gender,
             'idcard': man.idcard} for man in session.query(Person).all()]
    op.bulk_insert(person_table, data)

    # person = sa.Table(
    #     'person',
    #     sa.MetaData(),
    #     sa.Column('person_id', sa.Integer),
    #     sa.Column('nickname', sa.String(64)),
    #     sa.Column('gender', sa.Integer),
    #     sa.Column('idcard', sa.String(20))
    # )
    #
    # person_bk = sa.Table(
    #     'person_bk',
    #     sa.MetaData(),
    #     sa.Column('person_id', sa.Integer),
    #     sa.Column('nickname', sa.String(64)),
    #     sa.Column('gender', sa.Integer),
    #     sa.Column('idcard', sa.String(20))
    # )
    #
    # con = op.get_bind()
    # bk_data = con.execute(person.select())
    # for man in bk_data:
    #     con.execute(
    #         # inset data use orm will get 1 + 1 problem
    #         person_bk.insert().values(
    #             person_id=man.person_id,
    #             nickname=man.nickname,
    #             gender=man.gender,
    #             idcard=man.idcard
    #         )
    #     )

    with op.batch_alter_table('person') as batch_op:
        batch_op.drop_column('idcard')


def downgrade():
    # op.add_column('person', sa.Column('idcard', sa.String(length=20), nullable=True))
    op.drop_table('person')
    op.rename_table('person_bk', 'person')
