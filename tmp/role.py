from sqlalchemy import Column, Integer, String
import sys
sys.path.append("/Users/data/Desktop/cindy/gomi/npp/alembic/t1")

from Models import Base


class Role(Base):
    __tablename__ = 'role'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    role_name = Column('name', String(50))
