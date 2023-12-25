#write a python program which will read all the records from employee table--select Query
#selectrecordsex2.py
import cx_Oracle
def  recordsselect():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee")
		records=cur.fetchmany(3)
		for record in records:
			for val in record:
				print("{}".format(val), end=" ")
			print()
	except cx_Oracle.DatabaseError as db:
		print("Problem In Database:", db)

#main porogram
recordsselect()