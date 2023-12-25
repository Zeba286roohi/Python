#Program for demonstrating Functionality of Destructor.
#destex5.py
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






