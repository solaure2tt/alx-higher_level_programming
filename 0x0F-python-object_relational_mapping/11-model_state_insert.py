#!/usr/bin/python3
"""script that add a given State
   from a given database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state= State(name = 'Louisiana')
    session.add(state)
    session.commit()
    query = session.query(State).filter(State.name == 'Louisiana').first()
    print(state.id)