#University------>College----->Student
#Inhprog3.py
class Univ:
	def  getunivdet(self):
		self.uname=input("Enter  University Name:")
		self.uloc=input("Enter  University Location:")
	def dispunivdet(self):
		print("-"*50)
		print("\tUniversity details:")
		print("-"*50)
		print("University Name:{}".format(self.uname))
		print("University Location:{}".format(self.uloc))
		print("-"*50)

class College(Univ):
	def   getcolldet(self):
		self.cname=input("Enter College Name:")
		self.cloc=input("Enter  College Location:")
	def   dispcolldet(self):
		print("-"*50)
		print("\tCollege Details:")
		print("-"*50)
		print("College Name:{}".format(self.cname))
		print("College Location:{}".format(self.cloc))
		print("-"*50)

class Student(College):
	def  getstuddet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
	def dispstuddet(self):
		print("-"*50)
		print("\tStudent Details:")
		print("-"*50)
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-"*50)

#main program
s=Student()
s.getstuddet()
s.getcolldet()
s.getunivdet()
s.dispunivdet()
s.dispcolldet()
s.dispstuddet()


