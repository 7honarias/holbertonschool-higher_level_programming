#!/usr/bin/python3
import MySQLdb
from sys import argv

args = {
    'host':'localhost',
    'user': argv[1],
    'passwd':argv[2],
    'db': argv[3],
    'charset': 'utf8'
}

conn = MySQLdb.connect(**args)
cur = conn.cursor()

cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id")
query_row = cur.fetchall()

for row in query_row:
    print(row)

cur.close()
conn.close()
