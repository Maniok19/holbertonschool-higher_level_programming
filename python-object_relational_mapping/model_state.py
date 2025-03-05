#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine ('mysql+mysqldb://root:root@localhost:3306/sqlalchemy')