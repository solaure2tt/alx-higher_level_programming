#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    """ lists all cities from a given database """
    uName = sys.argv[1]
    pwd = sys.argv[2]
    dbn = sys.argv[3]
    lo = "localhost"
    db = MySQLdb.connect(host=lo, port=3306, user=uName, passwd=pwd, db=dbn)
    cur = db.cursor()
    qu = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states ON states.id = cities.state_id\
            ORDER BY cities.id ASC"
    cur.execute(qu)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
