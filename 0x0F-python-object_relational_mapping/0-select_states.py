#!/usr/bin/python3
"""This script lists all ``states`` from a given database."""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name,
                         charset="utf8")
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
