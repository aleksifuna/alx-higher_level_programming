#!/usr/bin/python3
"""This module supplies a script that filters and lists all states in a db """
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
    qry = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(qry)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
