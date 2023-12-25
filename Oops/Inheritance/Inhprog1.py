#Inhprog1.py
class C1:
	def  fun1(self):
		print("C1--fun1()")
	def fun3(self):
		print("C1-Fun3()")

class C2(C1):
	def fun2(self):
		print("C2--fun2()")

#main program
o2=C2()
o2.fun2()
o2.fun1()
o2.fun3()
