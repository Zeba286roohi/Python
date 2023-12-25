#This function computes sum of two numbers by using functions.
#Approach1.py
#Input<----Taking From Function Call
#Process<----Inside of Function Body
#Result/Output<----Function Call
def  addop(a,b):
	c=a+b
	return c

#main program
x=float(input("Enter First value:"))
y=float(input("Enter Second value:"))
result=addop(x,y)
print("sum=",result)