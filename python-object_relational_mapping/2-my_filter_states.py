#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

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
        cursor.execute("SELECT * FROM states WHERE CONVERT (`name` USING Latin1) COLLATE Latin1_General_CS = %s ORDER BY id ASC", (state,))
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
