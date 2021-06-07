import sqlite3
from sqlite3 import *
from PyQt5.QtCore import QDateTime

conn = sqlite3.connect("HospitalDatabase.db")
c = conn.cursor()
c.execute("create table if not exists patientDatabase(id integer primary key autoincrement, name text not null, dateOfBirth text, gender text not null, phone text not null, address text, email text)")
c.execute("create table if not exists serviceDatabase(id integer primary key autoincrement, patientId integer not null, serviceDate text, symptom text, diagnosis text, prescription text, comment text, billingId integer)")
c.execute("create table if not exists billingDatabase(id integer primary key autoincrement, patientId integer not null, serviceId integer not null, amount integer, comment text)")
c.execute("create table if not exists hospitalInfoDatabase(hospitalName text, doctorName text, logoDir text)")

def insertPatientData(conn, profile):
    sql='''INSERT INTO patientDatabase(name,gender,dateOfBirth,phone,address,email) values(?,?,?,?,?,?)'''
    cur=conn.cursor()
    cur.execute(sql, profile)

def updatePatientData(conn, profile):
    sql='''UPDATE patientDatabase set name=?,gender=?,dateOfBirth=?,phone=?,address=?,email=? where id=?'''
    cur=conn.cursor()
    cur.execute(sql, profile)

def insertServiceData(conn, service):
    sql='''INSERT INTO serviceDatabase(patientId, serviceDate, symptom, diagnosis, prescription) values(?,?,?,?,?)'''
    cur=conn.cursor()
    cur.execute(sql, service)

if __name__=="__main__":
    #record=(3,"2020-05-02/13:50:16","Mild cold","fever","take some rest")
    #insertServiceData(conn,record)
    c.execute("select * from hospitalInfoDatabase")
    rows=c.fetchall()
    conn.commit()
    for row in rows:
        print(row)
    conn.close()

