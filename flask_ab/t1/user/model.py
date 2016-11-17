# from application.const import USER_TABLE_NAME, GROUP_TABLE_NAME
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
# # from sqlalchemy.orm import relationship
# # from application.group.model import Group
# from application.core import db
from datetime import datetime
from shit import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    name = Column(String(10))
    password = Column(String(50))
    date_created = Column(DateTime, default=datetime.now())
    auth = Column(Boolean, default=True)
    # group = Column(String(100))
    group_id = Column(String, ForeignKey('{}.id'.format('group')), nullable=False)
    # group = relationship('Group', back_populates=USER_TABLE_NAME)
    addus = Column(String(100))

    def __repr__(self):
        return "<User (name='{}')".format(self.name)
