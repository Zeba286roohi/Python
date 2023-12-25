#This program accepts two from  KBD (end user) and gets the result
#divdemo.py
from divop import division
from kvr import KvrDivisionError  as KS
try:
	a=int(input("Enter Value of a:"))
	b=int(input("Enter Value of b:"))
	result=division(a,b) # Function call
except KS:
	print("\nDon't enter zero for den...")
except ValueError:
	print("\nDon't enter strs / alpha-numerics/symbols")
except :
	print("Some thing went wrong!")
else:
	print("Div=",result)
finally:
	print("I am from finally block")


#Phase-3: development of main program for handling the exception (try and except blocks)