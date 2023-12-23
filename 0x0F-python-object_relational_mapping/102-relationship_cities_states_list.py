#!/usr/bin/python3
"""
Lists all state objects and corresponding city object
"""
if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_objs = session.query(State).outerjoin(City).\
        order_by(State.id, City.id).all()
    for state in state_objs:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
