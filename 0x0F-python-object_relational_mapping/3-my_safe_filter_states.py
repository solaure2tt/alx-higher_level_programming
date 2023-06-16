#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    """ displays all values in the states table
        that is safe from MySQL injections
    """
    uName = sys.argv[1]
    pwd = sys.argv[2]
    dbn = sys.argv[3]
    val = sys.argv[4]
    lo = "localhost"
    db = MySQLdb.connect(host=lo, port=3306, user=uName, passwd=pwd, db=dbn)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(val)s ORDER BY id ASC",
                {'val': val})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
