#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


uName = sys.argv[1]
pwd = sys.argv[2]
dbn = sys.argv[3]
valstate = sys.argv[4]
lo = "localhost"
db = MySQLdb.connect(host=lo, port=3306, user=uName, passwd=pwd, db=dbn)
cur = db.cursor()
qu = "SELECT cities.name\
        FROM cities\
        JOIN states ON states.id = cities.state_id\
        WHERE states.name = '{}'\
        ORDER BY cities.id ASC".format(valstate)
cur.execute(qu)
rows = cur.fetchall()
res = ""
i = 1
for row in rows:
    for col in row:
        if i == 1:
            res = col
            i = i + 1
        else:
            res = res + ', ' + col
print(res)
cur.close()
db.close()
