#!/usr/bin/python3
""" class city
"""
from model_state import Base
from sqlalchemy import Column, Integer, String

"""declaration class"""


class City(Base):
    """declared columns"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)
