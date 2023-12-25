#hybridinh.py
class C1:
	def   x(self):
		print("C1--x()")
	def   __init__(self):
		print("C1-- const")

class C2(C1):
	def   x(self):
		print("C2--x()")
	def   __init__(self):
		print("C2-- const")

class C3(C1):
	def   x(self):
		print("C3--x()")
	def   __init__(self):
		print("C3-- const")

class C4(C2,C3):
	def   __init__(self):
		C1.__init__(self)
		C2.__init__(self)
		C3.__init__(self)

		print("C4-- const")
	def   x(self):
		print("C4--x()")
		C1.x(self)
		C2.x(self)
		C3.x(self)

o4=C4()
print("----------------------------")
o4.x()