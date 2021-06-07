import sqlite3
from sqlite3 import *
conn=sqlite3.connect("hospitalDatabase.db")
c=conn.cursor()
c.execute("select patientDatabase.name, serviceDatabase.serviceDate, billingDatabase.amount, billingDatabase.comment from ((billingDatabase inner join patientDatabase on patientDatabase.id=billingDatabase.patientId) inner join serviceDatabase on serviceDatabase.id=billingDatabase.serviceId) where billingDatabase.id=?",(str(1)))
rows=c.fetchall()
for row in rows:
    print(row)