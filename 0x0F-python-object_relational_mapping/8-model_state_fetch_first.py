#!/usr/bin/python3
""" 8. First state
script that prints the first State object from the database hbtn_0e_6_usa
./8-model_state_fetch_first.py vagrant pass hbtn_0e_6_usa
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

    first_result = session.query(State).first()
    if first_result:
        print("{}: {}".format(first_result.id, first_result.name))
    else:
        print("Nothing")
