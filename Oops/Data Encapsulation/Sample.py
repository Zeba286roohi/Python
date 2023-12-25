#Sample.py
class Sample:
	def __init__(self):
		self.__a=10
		self.b=20
		print("Val of a in constructor={}".format(self.__a)) # # Valid to access
		print("Val of b in constructor={}".format(self.b))
		
	def  getvalues(self):
		print("Val of a in getvalues()={}".format(self.__a))  # Valid to access
		print("Val of b in getvalues()={}".format(self.b))

	
#main program
s=Sample()
s.getvalues()
#print(s.a,s.b)  Invalid to access 