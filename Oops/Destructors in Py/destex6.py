#Program for demonstrating Functionality of Destructor.
#destex6.py
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
eo2=eo1 # Deep Copy
eo3=eo1 # Deep Copy   # Here GC calls Desturctor Only once bcoz eo1,eo2,eo3 are pointing 
                                        #single memory space.

#no longer interested to maintain object eo1
print("no longer interested to maintain object eo1:")
eo1=None #  Here the  GC will not call Destructor forcefully bcoz still eo2 and eo3 pointing to same memory space .
time.sleep(5)
print("no longer interested to maintain object eo2:")
eo2=None #  Here the  GC will not call Destructor forcefully bcoz still eo3 pointing to same memory space .
time.sleep(5)
print("Program execution ended :")
time.sleep(5)
# Here the  GC will call Destructor automatically and eliminates  same memory space of  eo3 .


