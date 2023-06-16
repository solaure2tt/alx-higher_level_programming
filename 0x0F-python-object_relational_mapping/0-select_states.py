#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


uName = sys.argv[1]
pwd = sys.argv[2]
dbn = sys.argv[3]
lo = "localhost"
db = MySQLdb.connect(host=lo, port=3306, user=uName, passwd=pwd, db=dbn)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
