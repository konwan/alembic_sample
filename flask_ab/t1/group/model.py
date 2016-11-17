# from application.core import db
# from application.const import GROUP_TABLE_NAME
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from talist.model import TaList
from user.model import User
from shit import db


class Group(db.Model):
    __tablename__ = 'group'
    id = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    gcp_project_id = Column(String(100), nullable=False)
    code = Column(String(100), nullable=False)
    date_deleted = Column(DateTime)
    date_created = Column(DateTime)
    # members = Column(String, nullable=False)
    latest_table_time = Column(DateTime)

    talists = relationship('TaList', back_populates='group')
    users = relationship('User', back_populates='group')
    addgp = Column(String(100))

    def __repr__(self):
        return "<Group(name='{}')".format(self.name)

TaList.group = relationship('Group', back_populates='talists')
User.group = relationship('Group', back_populates='users', passive_updates=False)
