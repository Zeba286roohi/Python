#This program display the content of any object by using static method
#StaticMethodEx6.py
class Employee:
	def readempvalues(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))

class Student: 
	def readstudvalues(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		self.cname=input("Enter Student Collegen Name:")

class Teacher : 
	def readteachervalues(self):
		self.tid=int(input("Enter Teacher ID:"))
		self.tname=input("Enter Teacher Name:")

class Information:
	@staticmethod
	def  showinfo(kvr):
		print("="*50)
		print("Number of Value={}".format(len(kvr.__dict__)))
		print("-"*50)
		for k,v in kvr.__dict__.items():
			print("\t{}--->{}".format(k,v))
		print("="*50)

#main program
e=Employee()
s=Student()
t=Teacher()
#read employee data
e.readempvalues()
#read Student data
s.readstudvalues()
#read teacherdata
t. readteachervalues()
print("Employee Data")
print("-------------------------------------")
Information.showinfo(e) # calling Static Method
print("-------------------------------------")
print("Student Data")
print("-------------------------------------")
Information.showinfo(s) # calling Static Method
print("-------------------------------------")
print("Teacher Data")
print("-------------------------------------")
Information.showinfo(t) # calling Static Method
print("-------------------------------------")
