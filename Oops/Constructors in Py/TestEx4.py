#TestEx4.py
class Test:
	def __init__(self,a=1,b=2):   # Constructors--Object Initlization
		print("i am from Default / Parameterized Constructor")
		self.a=a
		self.b=b
		print("="*50)
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("="*50)
#main program
t1=Test()						# object creation
t2=Test(100,200)            # object creation
t3=Test(20,30)

