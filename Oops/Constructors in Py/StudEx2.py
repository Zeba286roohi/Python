#StudEx2.py
class Student:
	def __init__(self):   # Constructors--Object Initlization
		print("i am from Constructor")
		self.sno=10
		self.name="Raj"
		self.marks=44.44
	



#main program
s=Student()
# object creation
print("content of s during object creation=",s.__dict__)
