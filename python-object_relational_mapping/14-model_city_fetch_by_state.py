#!/usr/bin/python3
"""
super super super cooooooooool
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session\
        .query(City, State).filter(State.id == City.state_id).all()
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
