#!/usr/bin/python3
""" 7. All states via SQLAlchemy
script that lists all State objects from the database hbtn_0e_6_usa
./7-model_state_fetch_all.py vagrant pass hbtn_0e_6_usa
"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for instance in states:
        print("{}: {}".format(instance.id, instance.name))

    session.close()
