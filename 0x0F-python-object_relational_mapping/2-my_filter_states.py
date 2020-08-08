#!/usr/bin/python3
"""
2. Filter states by user input
script that takes in an argument and displays all values in the
'states' table of 'hbtn_0e_0_usa' where name matches the argument.

usage ./2-my_filter_states.py <mysql username> <mysql passwd>
<database name> <state name searched>
example: ./2-my_filter_states.py vagrant pass hbtn_0e_0_usa 'Arizona'
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ displays all values in the 'states' table
    where name matches the argument """

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}' \
    ORDER BY states.id ASC;".format(sys.argv[4]))

    for elem in cur:
        print(cur.fetchone())

    cur.close()
