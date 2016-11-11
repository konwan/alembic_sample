from sqlalchemy import Column, Integer, String
import sys
sys.path.append("/Users/data/Desktop/cindy/gomi/npp/alembic/t1")
from Models import Base


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_name = Column('name', String(50))
