#!/usr/bin/python3
# List that start in N

import MySQLdb

from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,  user=username,
                           passwd=password,
                           db=database, charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_row = cur.fetchall()

    for row in query_row:
        print(row)

    cur.close()
    conn.close()
