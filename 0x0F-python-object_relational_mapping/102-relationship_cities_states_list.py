#!/usr/bin/python3
"""
Script that prints all
"""
import sys
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State).order_by(State.id).all()
    for state in query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
