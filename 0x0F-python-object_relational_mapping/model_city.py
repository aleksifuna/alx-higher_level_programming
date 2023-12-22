#!/usr/bin/python3
"""
module supplies one class defination (city)
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    city class that inherits from Base

    Attributes:
    id: city id
    name: Name of city
    state_id: the city's state id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
