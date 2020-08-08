#!/usr/bin/python3
"""
1. Filter states
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

usage ./1-filter_states.py <mysql username> <mysql passwd> <database name>
example: ./1-filter_states.py vagrant pass hbtn_0e_0_usa
"""
import MySQLdb
import sys


def states_starting_N():
    """  lists all states with a name starting with N """

    if len(sys.argv) != 4:
        return

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id;")
    for elem in cur:
        print(cur.fetchone())

    cur.close()

if __name__ == "__main__":
    states_starting_N()
