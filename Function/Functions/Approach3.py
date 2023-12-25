#This function computes sum of two numbers by using functions.
#Approach3.py
#Input<----Taking from  Function calls
#Process<----Inside of Function Body
#Result/Output<----Inside of Function Body
def  addop(x,y):
	z=x+y
	print("sum(%0.2f,%0.2f)=%0.2f" %(x,y,z))

#main program
a,b=float(input("Enter First Value:")),float(input("Enter Second Value:"))
addop(a,b)
