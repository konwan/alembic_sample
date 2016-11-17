import enum
# from application.core import db
# from application.const import TALIST_TABLE_NAME, GROUP_TABLE_NAME
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Enum, Integer
from sqlalchemy.orm import relationship
from shit import db


class TalistStatus(enum.Enum):
    pending = 100
    processing = 110
    success = 0
    failure = 200


class TaList(db.Model):
    __tablename__ = 'ta'
    id = Column(String(100), primary_key=True)
    name = Column(String(100))
    status = Column(Enum(TalistStatus))
    # status = Column(Integer)
    date_created = Column(DateTime)
    date_deleted = Column(DateTime)
    target_type = Column(String(100))
    product = Column(String(100))
    bq_table = Column(String(100))
    date_for_calculate = Column(DateTime)
    date_campaign_start = Column(DateTime)
    date_campaign_end = Column(DateTime)
    target_member_required = Column(String(100))
    member_email_required = Column(Boolean)
    member_mobile_required = Column(Boolean)
    exclude_talist = Column(String(100))
    group_id = Column(String(100), ForeignKey('{}.id'.format('group')), nullable=False)
    # group = relationship('Group', back_populates='talists')
    addta = Column(String(100))

    def __repr__(self):
        return "<TaList(name='{}')".format(self.name)
