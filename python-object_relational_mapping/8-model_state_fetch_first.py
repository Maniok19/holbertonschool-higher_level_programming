#!/usr/bin/python3
"""
super super super cooooooooool
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).order_by(State.id).first()
    if not results:
        print("Nothing")
    else:
        print("{}: {}".format(results.id, results.name))
