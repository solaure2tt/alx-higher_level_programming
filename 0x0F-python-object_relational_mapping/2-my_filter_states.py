#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    """ displays all values in the states table of a given databes
        where name matches the argument
    """
    uName = sys.argv[1]
    pwd = sys.argv[2]
    dbn = sys.argv[3]
    val = sys.argv[4]
    lo = "localhost"
    db = MySQLdb.connect(host=lo, port=3306, user=uName, passwd=pwd, db=dbn)
    cur = db.cursor()
    que = "SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
           COLLATE Latin1_General_CS = '{}' ORDER BY id ASC;".format(val)
    cur.execute(que)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
