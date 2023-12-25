#write a python program which will insert employee number, ename,salary and company name as a record in employee table of oracle database
#emp.py---file name and acts as module name
import cx_Oracle # step-1
def   empinsert():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl") #step-2
		cur=con.cursor()  # step-3
		#design and execute the query
		iq="insert into employee values(105,'Siva',4.5,'HCL') "
		cur.execute(iq)  
		con.commit()
		print("Number of records inserted :{}".format(cur.rowcount)) # 1
		print("Employee Record Inserted successfully in Employee table:")

	except cx_Oracle.DatabaseError as db:
		print("Problem in Database:",db)

