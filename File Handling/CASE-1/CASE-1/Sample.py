#Sample.py
class  KvrDivisionError(Exception):pass # Development of Programmer-defined Exception sub class

def   division(a,b): # Development a Function which will hit programmer-defined exception
	if(b==0):
		raise KvrDivisionError  # Hitting or generating or raising an exception when cond is satisfied.
	else:
		return (a/b)

#main program----- development of main program for handling the exception.
try:
	a=int(input("Enter Value of a:"))
	b=int(input("Enter Value of b:"))
	result=division(a,b) # Function call
except KvrDivisionError:
	print("\nDon't enter zero for den...")
except ValueError:
	print("\nDon't enter strs / alpha-numerics/symbols")
else:
	print("Div=",result)
finally:
	print("I am from finally block")