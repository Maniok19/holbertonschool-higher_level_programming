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

    db = None
    cursor = None
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                       FROM cities JOIN states \
                       ON cities.state_id = states.id ORDER BY  id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        exit(1)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
