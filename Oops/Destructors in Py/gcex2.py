#Program for demonstrating Functionality of Destructor.
#gcex2.py
import  time,gc
class Employee:
	def __init__(self,eno,ename):
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))
	def  __del__(self):
		print("\nDestructor called by Garbage Collector")

#mainm program
print("is GC enabled =",gc.isenabled() )  # True
print("Program execution started:")
gc.disable()
print("is GC enabled after disable() =",gc.isenabled() )  # False
eo1=Employee(10,"RS")
eo2=Employee(20,"DR")
eo3=Employee(30,"TR")
print("Program execution ended")
time.sleep(5)
