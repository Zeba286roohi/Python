#write a python program which will alter the employee table,change the column size and add new cloumn
#alterwithadd.py
import cx_Oracle  # step-1
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")  #step-2
	cur=con.cursor()  # step-3
	#design the query and execute----step-4
	aq="alter table employee add(cname varchar2(10))"
	cur.execute(aq)
	print("Employee Table altered  Sucecssfully in Oracle DB--verify") # step-5
except cx_Oracle.DatabaseError as db:
	print("\nProblem in database:", db)


