#StudEx4.py
class Student:
	def __init__(self,sno,sname):   # Constructors--Object Initlization
		print("i am from Parameterized Constructor")
		self.sno=sno
		self.name=sname
	def  dispstuddet(self):
		print("="*50)
		print("Student Number={}".format(self.sno))
		print("Student Name={}".format(self.name))
#main program
s1=Student(10,"Rossum")             # object creation
s2=Student(20,"Gosling")             # object creation
s3=Student(30,"Travis")                 # object creation
s4=Student(40,"kvr")
s1.dispstuddet()
s2.dispstuddet()
s3.dispstuddet()
s4.dispstuddet()
