#abstractclass.py
class Human:
	def   operation(self ):pass   # null body methods

class Teacher(Human):
	def operation(self):
		print("Teacher Takes the class and It is teacher operation")

class BusinessMan (Human):
	def  operation(self):
		print("Business do the Business  and It is Business operation")

class SE (Human):
	def  operation(self):
		print("SE developes the projects and its is SE Operation")

#main program
t=Teacher()
t.operation()
bm=BusinessMan()
bm.operation()
s=SE()
s.operation()


