#Inhprog2.py
class C1:
	def  fun1(self):
		print("C1--fun1()")
	def fun3(self):
		print("C1-Fun3()")

class C2(C1):
	def fun2(self):
		print("C2--fun2()")
		self.fun1() # here  we are calling base class Methods from derived class methods
		self.fun3() # here  we are calling base class Methods from derived class methods
		

#main program
o2=C2()
o2.fun2()
