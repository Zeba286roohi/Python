#Program for demonstrating Functionality of Destructor.
#destex2.py
import time
class Employee:
	def __init__(self,eno,ename):
		self.eno=eno
		self.ename=ename
		print("\t{}\t{}".format(self.eno,self.ename))

#mainm program
print("Program execution started:")
eo1=Employee(10,"RS")
eo2=Employee(20,"DR")
print("Program execution ended")
time.sleep(5)