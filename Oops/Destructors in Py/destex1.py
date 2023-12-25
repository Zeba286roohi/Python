#Program for demonstrating Functionality of Destructor.
#destex1.py
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
print("Program execution ended")
time.sleep(5)
