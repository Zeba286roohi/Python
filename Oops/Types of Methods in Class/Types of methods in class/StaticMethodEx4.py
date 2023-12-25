#Program demonstrating Static Methods
#StaticMethodEx4.py
class Sample:
	@staticmethod
	def  func1():
		print("I am from static Method--func1():")
	@staticmethod
	def  func2():
		print("I am from static Method--func2():")
	def  func3(self):
		print("I am from Instance Method--func3():")
		Sample.func2()#calling Static Method
		self.func1()#calling Static Method

#main program
s=Sample()
s.func3()
