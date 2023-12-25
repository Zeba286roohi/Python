#StudEx3.py
class Student:
	def __init__(self):   # Constructors--Object Initlization
		print("i am from Default Constructor")
		self.sno=int(input("Enter Student Number:"))
		self.name=input("Enter Student Name:")


#main program
s1=Student()             # object creation
print("content of s1 during object creation=",s1.__dict__)
s2=Student()             # object creation
print("content of s2 during object creation=",s2.__dict__)
s3=Student()
print("content of s3 during object creatin=",s3.__dict__)
