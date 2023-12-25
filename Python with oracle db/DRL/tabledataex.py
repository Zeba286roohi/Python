#write a python program which will display all the records of any table along with column names
#tabledataex.py
import cx_Oracle
def  allrecords():
	try:
		con=cx_Oracle.connect("scott/tiger@localhost/orcl")
		cur=con.cursor()
		tname=input("Enter table name:")
		cur.execute("select * from %s" %tname)
		#printing column names
		print("="*70)
		for colname in [colinfo[0]  for colinfo in cur.description]:
			print("{}".format(colname),end="   ")
		print()
		print("="*70)
		#display records of table
		#nor=0
		records=cur.fetchall()
		for record in records:
			#nor=nor+1
			for val in record:
				print("{}".format(val),end="  ")
			print()
		print("="*70)
		print("Total Number of Records={}".format(len(records)))
		print("="*70)
	except cx_Oracle.DatabaseError as db:
		print("Problem In Database:", db)
#main porogram
allrecords()
