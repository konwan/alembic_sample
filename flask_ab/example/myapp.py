#!/usr/bin/env python

import argparse
import flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Foo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bar = db.Column(db.Text)
    baz = db.Column(db.Text)


def create_app():
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('conf.py')
    db.init_app(app)
    return app


manager = Manager(create_app)


@manager.option('alembic_args', nargs=argparse.REMAINDER)
def alembic(alembic_args):
    from alembic.config import CommandLine
    CommandLine().main(argv=alembic_args)


@manager.command
def syncdb():
    db.create_all()
    alembic(['stamp', 'head'])

@manager.command
def revision(message=None):
    if message is None:
        message = raw_input('revision name: ')
    return alembic(['revision', '--autogenerate', '-m', message])

@manager.command
def upgrade(revision='head'):
    return alembic(['upgrade', revision])

@manager.command
def downgrade(revision):
    return alembic(['downgrade', revision])


if __name__ == '__main__':
    manager.run()
