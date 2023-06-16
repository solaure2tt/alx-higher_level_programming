#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    """lists all states with a name starting with N
        from a given database
    """
    uName = sys.argv[1]
    pwd = sys.argv[2]
    dbn = sys.argv[3]
    lo = "localhost"
    db = MySQLdb.connect(host=lo, port=3306, user=uName, passwd=pwd, db=dbn)
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states\
                    WHERE  CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS \
                    LIKE 'N%' ORDER BY id ASC;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
