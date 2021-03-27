#!/usr/bin/python3
"""contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

""" class State """


class State(Base):
    """ init class columns table"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relation('City', backref='state', cascade='all, delete')
