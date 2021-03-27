#!/usr/bin/python3
"""take care of injercion
"""
from sys import argv

import MySQLdb


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]
    match = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database, charset='utf8')

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (match,))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
