#write a python program which will create employe table with empno,empname and salary in oracle database
#tablecreate.py
import cx_Oracle  # step-1
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")  #step-2
	cur=con.cursor()  # step-3
	#design the query and execute----step-4
	ctq="create table employee(eno number(2) primary key,ename varchar2(10) not null, sal number(8,2) )  "
	cur.execute(ctq)
	print("Employee Table Created Sucecssfully in Oracle DB--verify") # step-5
except cx_Oracle.DatabaseError as db:
	print("\nProblem in database:", db)

