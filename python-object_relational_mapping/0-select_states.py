#!/usr/bin/python3
"""
This module makes a query to the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
