#Program for demonstrating Functionality of Destructor.
#destex3.py
import  time
class Employee:
	def __init__(self,eno,ename):
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))
	def  __del__(self):
		print("\nDestructor called by Garbage Collector")

#mainm program
print("Program execution started:")
eo1=Employee(10,"RS")
eo2=Employee(20,"DR")
eo3=Employee(30,"TR")
#no longer interested to maintain object eo1
print("no longer interested to maintain object eo1:")
eo1=None   # Here the memory space eo1 collected by GC-forcefully
time.sleep(5)
#no longer interested to maintain object eo2
print("no longer interested to maintain object eo2:")
eo2=None   # Here the memory space eo2 collected by GC -forcefully
time.sleep(5)
print("Program execution Execution Completed:")
time.sleep(5)
# Here the memory space eo3 collected by GC -automatically








