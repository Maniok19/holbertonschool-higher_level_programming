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
        cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC",(state,))
        rows = cursor.fetchall()
        for row in rows:
            result = row[0]
            if row != rows[-1]:
                print(result, end = ", ")
            else:
                print(result)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        exit(1)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
