#!/usr/bin/python3
"""
wabababababababjdbjbj
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
                    FROM cities JOIN states \
                    ON cities.state_id = states.id \
                    WHERE CONVERT (states.name USING Latin1) \
                    COLLATE Latin1_General_CS = %s \
                    ORDER BY cities.id ASC", (state,))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
