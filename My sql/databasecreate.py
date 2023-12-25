#Program for creating a database on the name of "batch9am"
#databasecreate.py
import mysql.connector
try:
	conobj=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root")
	cur=conobj.cursor()
	#design the query and execute
	dq="create database batch9am" 
	cur.execute(dq)
	print("Data Base created in MySQL and Verify:")
except mysql.connector.DatabaseError as d:
	print("Problem in Data Base:",d)
