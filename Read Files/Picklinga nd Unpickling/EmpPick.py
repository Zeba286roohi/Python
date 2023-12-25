#write a python program which will accept employee details such as employee number , employee name, salary and company name and store employee details in a file by using pickling concept
#EmpPick.py
import pickle,sys
def   stroreempdata():
	with open("emp.data","ab") as fp:
		while(True):
			try:
				#accept employee details
				print("-"*50)
				eno=int(input("Enter Employee Number:"))
				ename=input("Enter Employee Name:")
				sal=float(input("Enter Employee Salary:"))
				cname=input("Enter Employee Company:")
				#create an empty list
				lst=[]
				#append the employee data
				lst.append(eno)
				lst.append(ename)
				lst.append(sal)
				lst.append(cname)
				#write or save entire object data to File----dump() of pickle module
				pickle.dump(lst,fp)
				print("-"*50)
				print("Employee Record Saved in a file:")
				print("-"*50)
				ch=input("Do u want to insert another Employee Record(yes/no):")
				if(ch.lower()=="no"):
					sys.exit()
			except ValueError:
				print("Don't enter strs/sysmbols/alpha-numerics for number and sal:")

#main program
stroreempdata()



