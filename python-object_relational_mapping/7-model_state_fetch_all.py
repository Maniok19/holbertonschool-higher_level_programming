#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format\
                           (sys.argv[1],\
                            sys.argv[2],\
                            sys.argv[3]),\
                            pool_pre_ping=True)
    session = Session(engine)
    results = session.query(State).order_by(State.id).all()
    for result in results:
        print("{}: {}".format(result.id, result.name))
