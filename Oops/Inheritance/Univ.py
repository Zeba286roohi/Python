#Univ.py----File Name and acts as module
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
