#Program demonstrating Static Methods
#StaticMethodEx1.py
class Sample:
	@staticmethod
	def  func1():
		print("I am from static Method--func1():")
	@staticmethod
	def  func2():
		print("I am from static Method--func2():")

#main program
Sample.func1() # calling static Method
Sample.func2() # calling static Method
