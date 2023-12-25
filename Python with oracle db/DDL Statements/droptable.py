#write a python program which will alter the employee table,change the column size and add new cloumn
#droptable.py
import cx_Oracle  # step-1
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")  #step-2
	cur=con.cursor()  # step-3
	#design the query and execute----step-4
	cur.execute("drop table student")
	print("Student Table Dropped  Sucecssfully in Oracle DB--verify") # step-5
except cx_Oracle.DatabaseError as db:
	print("\nProblem in database:", db)


