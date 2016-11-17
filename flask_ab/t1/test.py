from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_alembic import Alembic
from datetime import datetime
from shit import app
from shit import db
from user.model import User
from talist.model import TaList
from group.model import Group


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/data/Desktop/cindy/gomi/npp/shit/no.db'
#
# db = SQLAlchemy(app)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# tt = User()


if __name__ == '__main__':
    with app.app_context():
        alembic = Alembic()
        alembic.init_app(app)
        alembic._clear_cache()

        alembic.rev_id = (lambda: datetime.now().strftime('%Y%m%dT%H:%M:%S'))
        # print(alembic.rev_id)
        print(alembic.heads())
        # print(alembic.branches())

        alembic.upgrade()
        # alembic.revision('change schema')
        # alembic.upgrade(target='20161115T18:31:44')
        # environment_context = alembic.env
        # alembic.downgrade(target="base")
        # print("sssssssssssss %s" % alembic.current())
        print(alembic.current()[0])
