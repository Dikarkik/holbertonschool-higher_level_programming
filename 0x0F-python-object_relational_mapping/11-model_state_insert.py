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

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")
    print(new_state.id)
    session.add(new_state)
    session.commit()
    session.close()
