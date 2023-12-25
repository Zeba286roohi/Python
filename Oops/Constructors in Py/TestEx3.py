#TestEx3.py
class Test:
	def __init__(self,a,b):   # Constructors--Object Initlization
		print("i am from Parameterized Constructor")
		self.a=a
		self.b=b
		print("="*50)
		print("Val of a={}".format(self.a))
		print("Val of b={}".format(self.b))
		print("="*50)
#main program

print("Enter Two Value for First Object:")
x=int(input())
y=int(input())
t1=Test(x,y)					# object creation
print("Enter Two Value forSecond Object:")
t2=Test(float(input()), float(input()))            # object creation
print("Enter Two Value for Third Object:")
t3=Test(input(), input() )			 # object creation