#Program for calculating Simple  Interest by using Classes and Objects
#SimpleInt.py
class SimpleInt:
	def  readvalues(self):
		self.p=float(input("Enter Principle Amount:"))
		self.t=float(input("Enter Time:"))
		self.r=float(input("Enter Rate Of Interest:"))
	
	def  calSimpleInt(self):
		self.si=(self.p*self.t*self.r)/100

	def   dispresult(self):
		print("="*50)
		print("Principle Amount:{}".format(self.p))
		print("Time :{}".format(self.t))
		print("Rate of Interest :{}".format(self.r))
		print("Simple Interest:{}".format(self.si))
		print("="*50)

#main program
si=SimpleInt()
si.readvalues()
si.calSimpleInt()
si.dispresult()
