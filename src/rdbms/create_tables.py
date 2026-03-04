from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Sequence,  ForeignKey, DateTime


class Base(DeclarativeBase):
    pass


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer,  Sequence("seq", start=1), primary_key=True)
    name = Column(String)


class Deployment(Base):
    __tablename__ = "deployments"
    id = Column(String, primary_key=True)
    db_name = Column(String)
    status = Column(Integer, ForeignKey("status.id"))
    username = Column(String)
    creation_time = Column(DateTime)

