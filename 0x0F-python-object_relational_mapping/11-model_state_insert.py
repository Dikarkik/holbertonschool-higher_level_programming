#!/usr/bin/python3
""" 11. Add a new state
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa

./11-model_state_insert.py vagrant pass hbtn_0e_6_usa
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

    name_to_add = "Louisiana"

    """ prevent repeated entry """
    result = session.query(State).filter(State.name.like(name_to_add)).first()
    if not result:
        new_state = State(name=name_to_add)
        session.add(new_state)
        session.commit()
        result = session.query(State)\
                        .filter(State.name.like(name_to_add))\
                        .first()
        print(result.id)

    session.close()
