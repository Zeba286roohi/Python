#polyex6.py-------with constructor
class C1:
	def __init__(self,a):  # Original Constructor
		print("C1--default Constructor and a={}".format(a))

class C2:
	def __init__(self,b):  # Original Constructor
		print("C2--default--constructor and b={}".format(b))
	
class C3(C2,C1):
	def __init__(self):  # Overridden Constructor
		print("C3--default--constructor")
		C1.__init__(self,10)
		C2.__init__(self,20)
	

#main program
o3=C3()
