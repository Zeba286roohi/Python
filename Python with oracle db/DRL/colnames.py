#write a python program which will read all the records from employee table--select Query
#colnames.py
import cx_Oracle
def  colnames():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from emp")
		colinfos=cur.description
		colnames= [colinfo[0]  for colinfo in colinfos]
		print("="*50)
		for colname in colnames:
			print("{}".format(colname),end="   ")
		print()
		print("="*50)
	except cx_Oracle.DatabaseError as db:
		print("Problem In Database:", db)
#main porogram
colnames()