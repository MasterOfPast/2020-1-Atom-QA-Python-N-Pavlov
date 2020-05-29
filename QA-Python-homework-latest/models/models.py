from sqlalchemy import Column, Integer, SmallInteger, VARCHAR, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class test_users(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(16), nullable=True)
    password = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(64), nullable=False)
    access = Column(SmallInteger, nullable=True)
    active = Column(SmallInteger, nullable=True)
    start_active_time = Column(Date, nullable=True)
