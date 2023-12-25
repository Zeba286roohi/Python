#Student.py----file name and acts as module name
from College import College
class Student(College):
	def  getstuddet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
		self.getcolldet()
		self.getunivdet()

	def dispstuddet(self):
		self.dispunivdet()
		self.dispcolldet()
		print("-"*50)
		print("\tStudent Details:")
		print("-"*50)
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-"*50)