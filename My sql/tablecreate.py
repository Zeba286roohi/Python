#write a python program which will create employee table with column name eno,ename,sal and cname in MYSQL
#tablecreate.py
import mysql.connector
try:
	conobj=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch9am" )
	cur=conobj.cursor()
	#design the query and execute
	tq="create table student (sno  int primary key, sname varchar(10) not null, marks  real not null, cname varchar(10) not null )"
	cur.execute(tq)
	print("Table  created in batch9am database of MySQL and Verify:")
except mysql.connector.DatabaseError as d:
	print("Problem in Data Base:",d)
