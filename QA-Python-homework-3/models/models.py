from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Demon(Base):
    __tablename__ = 'demons'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    True_name = Column(String(50), nullable=False)
    Heavenly_name = Column(String(30), nullable=False)
    reliase_date = Column(Date, nullable=False, default='2020-01-01')

    def __repr__(self):
        return f"<demons(" \
               f"id='{self.id}'," \
               f"name='{self.name}', " \
               f"True_name='{self.True_name}', " \
               f"Heavenly_name='{self.Heavenly_name}'," \
               f"reliase_date='{self.reliase_date}'" \
               f")>"


class Log(Base):
    __tablename__ = 'logs_nginx'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    date = Column(String(30), nullable=False)
    method = Column(String(6), nullable=False)
    request = Column(String(60), nullable=False)
    status = Column(Integer, nullable=False)
    body_bytes_sent = Column(Integer, nullable=False)
    http_user_agent = Column(String(60), nullable=False)
