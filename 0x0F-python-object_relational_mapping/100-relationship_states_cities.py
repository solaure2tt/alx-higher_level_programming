#!/usr/bin/python3
"""script that add the State “California” with the City “San Francisco”
   from a given database
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='California')
    newCi = City(state_id=state.id, name='San Francisco')
    state.cities.append(newCi)
    session.add(newCi)
    session.add(state)
    session.commit()
