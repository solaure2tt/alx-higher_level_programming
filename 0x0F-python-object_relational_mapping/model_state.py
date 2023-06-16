#!/usr/bin/python3
""" This module is to create a state model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb


Base = declarative_base()


class State(Base):
    """creation of the table states"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
