#!/usr/bin/python3
"""
This module supplies a list of cities
"""
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", [argv[4]])
    rows = cur.fetchall()
    results = []
    for i in rows:
        results.append(i[1])
    print(", ".join(results))
    cur.close()
    db.close()
