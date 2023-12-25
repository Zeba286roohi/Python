#polyex6.py-------with constructor
class C1:
	def __init__(self):  # Original Constructor
		print("C1--default Constructor")

class C2(C1):
	def __init__(self):  # Overridden Constructor
		print("C2--default--constructor")
		super().__init__()
		
class C3(C2):
	def __init__(self):  # Overridden Constructor
		print("C3--default--constructor")
		super().__init__()

#main program
o3=C3()
