#!/usr/bin/python3
"""
wabababababababjdbjbj
"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class City(Base):
    """
    city class
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
