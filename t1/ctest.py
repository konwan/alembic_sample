#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    person_id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(64), nullable=False)
    gender = sa.Column(sa.Integer)
    idcard = sa.Column(sa.String(20))


class Telephone(Base):
    __tablename__ = 'telephone'

    tel_id = sa.Column(sa.Integer, primary_key=True)
    person_id = sa.Column(sa.Integer, sa.ForeignKey('person.person_id'))
    telphone_no = sa.Column(sa.String(64))
    memo = sa.Column(sa.String(20))

if __name__ == "__main__":

    engine = sa.create_engine("sqlite:////Users/data/Desktop/cindy/gomi/npp/alembic/test.db")
    Base.metadata.create_all(engine)
