#This program stores stno,name and marks
#studentex6.py
class Student:
	def   readstuddata(self):
		print("-"*50)
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
		print("-"*50)
	def  dispstuddata(self):
		print("-"*50)
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Marks:{}".format(self.marks))
		print("-"*50)

#main program
s1=Student()
s2=Student()
print("Enter First Student Information:")
s1.readstuddata()
print("Enter Second Student Information:")
s2.readstuddata()
print("First Student Information:")
s1.dispstuddata()
print("Second Student Information:")
s2.dispstuddata()

