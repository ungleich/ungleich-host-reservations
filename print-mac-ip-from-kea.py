#!/usr/bin/env python3
# Carlos Ortigoza Dempster (carlos.ortigoza -at- ungleich.ch)
# 2016-11-05

import os
import psycopg2

HOST = os.environ['HOST']
DB = os.environ['DB']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']

try:
    conn = psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(DB, USER, HOST, PASSWORD))
except:
    print("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("""SELECT encode(dhcp_identifier, 'hex'), ipv4_address, hostname FROM hosts""")
rows = cur.fetchall()

print("dhcp_identifier\tipv4_address\thostname")
for row in rows:
    mac=":".join([row[0][i:i+2] for i in range(0, len(row[0]), 2)])
    print("{}\t{}\t{}".format(mac, row[1], row[2]))