#write a python program which will read all the records from employee table--select Query
#selectrecordsex1.py
import cx_Oracle
def  recordsselect():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee")
		while(True):
			rec=cur.fetchone()
			if(rec!=None):
				for val in rec:
					print("{}".format(val),end=" ")
				print()
			else:
				break
	except cx_Oracle.DatabaseError as db:
		print("Problem In Database:", db)


#main porogram
recordsselect()