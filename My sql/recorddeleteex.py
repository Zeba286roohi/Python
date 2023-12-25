#write a python program which will delete a record from employee table based on employee number.
#recorddeleteex.py
import mysql.connector
def empdelete():
	try:
		while(True):
			try:
				con=mysql.connector.connect(host="localhost",
															user="root",
															passwd="root",
															database="batch9am" )
				cur=con.cursor()  # step-3
				#accept employee data
				empno=int(input("Enter Employee Number:"))
				#design and execute  the query
				cur.execute("delete from employee where eno=%d" %empno)
				con.commit()
				if(cur.rowcount>0):
					print("{} Employee Record(s) delete from employee table:".format(cur.rowcount))
				else:
					print("Employee Record does not exists")
				print("="*50)
				ch=input("Do u want to delete another Record(yes/no):")
				if(ch.lower()=="no"):
					print("Thanks for using this program")
					break
			except ValueError:
				print("\nDon't enter strs/symbols/alpha-numerics for Emp Number ")
	except mysql.connector.DatabaseError as db:
		print("Problem in Database:",db)

#main program
empdelete()
