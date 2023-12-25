#This function computes sum of two numbers by using functions.
#Approach41.py
#Input<----Taking Inside of  Function body
#Process<----Inside of Function Body
#Result/Output<----Gives result Function Call
def  addop():
	k=float(input("Enter First Value:"))
	v=float(input("Enter Second Value:"))
	r=k+v
	return k,v,r # In python programming, return stmt can return either one value or multiple values

#main program
k1,v1,r=addop()  # Function call with multi line assignment
print("sum({},{})={}".format(k1,v1,r))
print("===========OR============")
result=addop()  # Function call with single line assignment
print("type of result var=",type(result)) # type of result var= <class 'tuple'>
print("sum({},{})={}".format(result[0],result[1],result[2]))
print("===========OR============")
print("sum({},{})={}".format(result[-3],result[-2],result[-1]))
