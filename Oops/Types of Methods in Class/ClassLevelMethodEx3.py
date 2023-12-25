#This program demonstartes about class Level method
#ClassLevelMethodEx3.py
class Employee:
	@classmethod       # Pre-defined decorator
	def  getcompnames(cls):
		cls.cname="IBM"  # Class Level Data Member
	@classmethod
	def  getcomploc(cls):
		cls.cloc="HYD"   # Class Level Data Member

	def getempdet(self):
		print("-"*50)
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))
		print("-"*50)
	def  dispempdet(self):
		print("-"*50)
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Salary:{}".format(self.sal))
		self.getcompnames()
		self.getcomploc()  # calling Class Level Methods from Instance Methods
		print("Employee Comp Name:{}".format(Employee.cname))
		print("Employee Comp Loc:{}".format(Employee.cloc))
		print("-"*50)
#main program
e1=Employee()
e2=Employee()
print("Enter First Employee Information:")
e1.getempdet()
print("Enter Second Employee Information:")
e2.getempdet()
print("\nFirst Employee Information:")
e1.dispempdet()
print("\nSecond Employee Information:")
e2.dispempdet()