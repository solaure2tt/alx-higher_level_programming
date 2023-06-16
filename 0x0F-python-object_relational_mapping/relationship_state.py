#!/usr/bin/python3
""" This module is to create a state model """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import MySQLdb


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """creation of the table states"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
