#!/usr/bin/python3
"""
4. Cities by states
script that lists all 'cities' from the database 'hbtn_0e_4_usa'

usage ./4-cities_by_state.py <mysql username> <mysql passwd> <database name>
example: ./4-cities_by_state.py vagrant pass hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ lists all 'cities' from the database """

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
     LEFT JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;")
    rows = cur.fetchall()

    for elem in rows:
        print(elem)

    cur.close()
