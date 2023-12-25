#write a python program which will read all the records from employee table--select Query
#colnamesdir.py
import cx_Oracle
def  colnames():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		tname=input("Enter table name:")
		cur.execute("select * from %s" %tname)
		print("="*50)
		for colname in [colinfo[0]  for colinfo in cur.description]:
			print("{}".format(colname),end="   ")
		print()
		print("="*50)
	except cx_Oracle.DatabaseError as db:
		print("Problem In Database:", db)
#main porogram
colnames()