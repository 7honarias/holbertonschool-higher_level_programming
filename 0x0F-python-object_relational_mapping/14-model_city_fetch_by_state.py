#!/usr/bin/python3
""" Script that print all City
"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    query_row = (session.query(City, State)
                 .filter(City.state_id == State.id).order_by(City.id).all())
    for row in query_row:
        print('{}: ({}) {}'.format(row.State.name, row.City.id, row.City.name))
    session.close()
