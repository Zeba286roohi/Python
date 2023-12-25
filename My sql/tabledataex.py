#write a python program which will display all the records of any table along with column names
#tabledataex.py
import mysql.connector
def  allrecords():
	try:
		con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch9am" )
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
		records=cur.fetchall()
		for record in records:
			for val in record:
				print("{}".format(val),end="  ")
			print()
		print("="*70)
		print("Total Number of Records={}".format(len(records)))
		print("="*70)
	except mysql.connector.DatabaseError as db:
		print("Problem In Database:", db)
#main porogram
allrecords()
