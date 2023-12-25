#College.py---file name and acts as module
from Univ import Univ
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