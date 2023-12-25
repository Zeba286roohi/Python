#This program accepts two from  KBD (end user) and gets the result
#divdemo1.py
from divop import division
from kvr import KvrDivisionError
try:
	a=int(input("Enter Value of a:"))
	b=int(input("Enter Value of b:"))
	result=division(a,b) # Function call
except (KvrDivisionError , ValueError):
	print("\nDon't enter zero for den...")
	print("\nDon't enter strs / alpha-numerics/symbols")
except :
	print("Some thing went wrong!")
else:
	print("Div=",result)
finally:
	print("I am from finally block")