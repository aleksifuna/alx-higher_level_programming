#!/usr/bin/python3
"""This module supplies a script that lists all states in a db """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
