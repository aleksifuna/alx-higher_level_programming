#!/usr/bin/python3
"""
prints the first state object from the db
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()
    Base.metadata.create_all(engine)
    states = session.query(State).filter(State.name == argv[4]).first()
    if states:
        print(states.id)
    else:
        print("Not found")
    session.close()
