#!/usr/bin/python3
""" 14. Cities in state """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ Defines City """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
