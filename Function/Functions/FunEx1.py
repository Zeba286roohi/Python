#This function computes sum of two numbers by using functions.
#FunEx1.py
def  addop(a,b):
	"""This program cal sum of two numbers"""
	c=a+b # here 'c' is called Local variable
	return c  # here return statement used to return the result from function body.

#main program
c=addop(10,20)  # Function call
print("sum=",c)
print("type of addop=", type(addop))
print("doc string of addop()=",   addop.__doc__)


