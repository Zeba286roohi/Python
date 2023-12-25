#Program demonstrating Static Methods
#StaticMethodEx5.py
class Sample:
	@classmethod
	def  func4(cls):
		print("I am from Class Method--func4():")
		cls.func1() # OR Sample.func1()---calling Static Method

	@staticmethod
	def  func1():
		print("I am from static Method--func1():")
	@staticmethod
	def  func2():
		print("I am from static Method--func2():")
		Sample.func4() # calling Class Level Method
	def  func3(self):
		print("I am from Instance Method--func3():")
		Sample.func2()#calling Static Method
		
#main program
s=Sample()
s.func3()
