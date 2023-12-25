#Program demonstrating Static Methods
#StaticMethodEx2.py
class Sample:
	@staticmethod
	def  func1():
		print("I am from static Method--func1():")
	@staticmethod
	def  func2():
		print("I am from static Method--func2():")

#main program
s=Sample()
s.func1() # calling static Method
s.func2() # calling static Method
