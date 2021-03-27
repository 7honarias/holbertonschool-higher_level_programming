#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    args = {
        'host': 'localhost',
        'port': 3306,
        'user': argv[1],
        'password': argv[2],
        'db': argv[3],
        'charset': 'utf8'
    }
    match = argv[4]

    conn = MySQLdb.connect(**args)
    cur = conn.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (match,))

    query_rows = cur.fetchall()
    isfirst = 0
    for row in query_rows:
        if isfirst != 0:
            print(", ", end="")
        print("{}".format(row[0]), end="")
        isfirst += 1
    print()
    cur.close()
    conn.close()
