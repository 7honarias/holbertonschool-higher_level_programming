#!/usr/bin/python3
# module print all table

import MySQLdb

from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
