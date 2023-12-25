#TestEx2.py
class Test:
	def __init__(self,a,b):   # Constructors--Object Initlization
		print("i am from Parameterized Constructor")
		self.a=a
		self.b=b
		print("="*50)
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("="*50)
		return (self.a+self.b)
		
#main program
t1=Test(10,20)					# object creation
t2=Test(100,200)            # object creation
t3=Test(1,2)			 # object creation
