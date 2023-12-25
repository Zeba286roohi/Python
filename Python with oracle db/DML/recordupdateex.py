#write a pythom program which will update salary of an emp,cname of an emp based on emp no
#recordupdateex.py
import cx_Oracle
def empupdate():
	try:
		while(True):
			try:
				con=cx_Oracle.connect("scott/tiger@localhost/orcl") #step-2
				cur=con.cursor()  # step-3
				#accept employee data
				empno=int(input("Enter Employee Number:"))
				newsal=float(input("Enter New salary for Employee:"))
				newcomp=input("Enter new Comp Name of Employee:")
				#design and execute  the query
				cur.execute("update employee set sal=%f , cname='%s' where eno=%d" %(newsal,newcomp,empno) )
				con.commit()
				if(cur.rowcount>0):
					print("{} Employee Record(s) updated in employee table:".format(cur.rowcount))
				else:
					print("Employee Record does not exists")
				print("="*50)
				ch=input("Do u want to update another Record(yes/no):")
				if(ch.lower()=="no"):
					print("Thanks for using this program")
					break
			except ValueError:
				print("\nDon't enter strs/symbols/alpha-numerics for Emp Number and Salary ")
	except cx_Oracle.DatabaseError as db:
		print("Problem in Database:",db)

#main program
empupdate()
