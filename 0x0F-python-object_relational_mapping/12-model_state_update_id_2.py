#!/usr/bin/python3
""" 12. Update a state
script that changes the name of a State object
from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico

./12-model_state_update_id_2.py vagrant pass hbtn_0e_6_usa
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

    state = session.query(State).get(2)
    state.name = "New Mexico"
    session.commit()
    session.close()
