#!/usr/bin/python3
"""
0. Get all states
script that lists all states from the database hbtn_0e_0_usa

usage ./0-select_states.py <mysql username> <mysql passwd> <database name>
example: ./0-select_states.py root root hbtn_0e_0_usa
"""
import MySQLdb
import sys


def lists_all_states():
    """ lists all states """
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    for elem in cur:
        print(cur.fetchone())

if __name__ == "__main__":
    lists_all_states()
