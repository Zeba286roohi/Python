#This program createas an object cursor
#cursorex.py
import mysql.connector
conobj=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root")
print("python program got connection from MYSQL")
cur=conobj.cursor()
print("cursor object created:")
print("type cur=",type(cur))  # type cur= <class 'mysql.connector.cursor.MySQLCursor'>
