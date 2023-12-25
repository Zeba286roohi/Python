#Program demonstrating Static Methods
#StaticMethodEx3.py
class Sample:
	@staticmethod
	def  func1():
		print("I am from static Method--func1():")
		Sample.func2() # calling static method
	@staticmethod
	def  func2():
		print("I am from static Method--func2():")

#main program
Sample.func1() # calling static method 