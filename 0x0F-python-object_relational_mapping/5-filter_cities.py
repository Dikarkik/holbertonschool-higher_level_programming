#!/usr/bin/python3
"""
5. All cities by state
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

usage ./5-filter_cities.py <mysql username> <mysql passwd>
<database name> <state name>
example: ./5-filter_cities.py vagrant pass hbtn_0e_4_usa Texas
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.name
                    FROM cities
                    LEFT JOIN states
                    ON cities.state_id=states.id
                    WHERE states.name=(%s)""", (sys.argv[4],)
                )

    rows = cur.fetchall()
    cities = []

    if rows:
        for elem in rows:
            cities.append(elem[0])

    print(", ".join(cities))

    cur.close()
    db.close()
