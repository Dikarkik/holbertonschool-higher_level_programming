#!/usr/bin/python3
""" 10. Get a state
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
./10-model_state_my_get.py vagrant pass hbtn_0e_6_usa Texas
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

    result = session.query(State).filter(State.name.like(sys.argv[4])).first()
    if result:
        print("{}".format(result.id))
    else:
        print("Not found")
