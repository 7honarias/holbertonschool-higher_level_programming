#!/usr/bin/python3
""" Script that deletes all State that contains the letter a
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session =  sessionmaker(engine)
    session = Session()
    query_rows = session.query(State).filter(State.name.like('%a%'))
    for row in query_rows:
        session.delete(row)
    session.commit()
    session.close()
