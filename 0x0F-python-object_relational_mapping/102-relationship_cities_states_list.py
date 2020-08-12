#!/usr/bin/python3
""" 17. From city
script that lists all City objects from the database hbtn_0e_101_usa

./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id).all()

    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
