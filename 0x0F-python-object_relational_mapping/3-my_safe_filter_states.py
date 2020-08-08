#!/usr/bin/python3
"""
3. SQL Injection...
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

usage ./3-my_safe_filter_states.py <mysql username> <mysql passwd>
<database name> <state name searched>
example: ./3-my_safe_filter_states.py vagrant pass hbtn_0e_0_usa 'Arizona'
SQL injection: ./3-my_safe_filter_states.py vagrant
pass hbtn_0e_0_usa"Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
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

    cur.execute("SELECT * FROM states WHERE name=(%s)\
    ORDER BY id ASC;", (sys.argv[4],))

    for elem in cur:
        print(cur.fetchone())

    cur.close()
    db.close()
