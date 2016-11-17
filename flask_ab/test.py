from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_alembic import Alembic
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/data/Desktop/cindy/gomi/npp/shit_2/no.db'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    name = Column(String(10))
    password = Column(String(50))
    date_created = Column(DateTime, default=datetime.now())
    auth = Column(Boolean, default=True)


if __name__ == '__main__':
    with app.app_context():
        alembic = Alembic()
        alembic.init_app(app)
        alembic._clear_cache()

        # alembic.rev_id = (lambda: datetime.now().strftime('%Y%m%dT%H:%M:%S'))
        # print(alembic.heads())
        # print(alembic.branches())

        # alembic.revision('change schema')
        alembic.upgrade()
        # alembic.upgrade(target='20161115T18:31:44')
        # environment_context = alembic.env
        # alembic.downgrade(target="base")
        # print("sssssssssssss %s" % alembic.current())
        print(alembic.current())

