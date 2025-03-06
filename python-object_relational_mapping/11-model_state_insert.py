#!/usr/bin/python3
"""
super super super cooooooooool
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


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
    session.add(State(name='Louisiana'))
    results = session.query(State).all()
    for result in results:
        print("{}: {}".format(result.id, result.name))
    session.commit()
