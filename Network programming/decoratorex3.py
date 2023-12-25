#decoratorex3.py
def cube(hyd):
	def operation1():
		x=hyd()
		res=x**3
		return res
	return operation1

def  square(kvr): 
	def   operation():
		n=kvr()
		res=n**2
		return res
	return operation

@cube
@square
def  getval():
	return (float(input("Enter a number:")))

#main program
result=getval()
print("result=",result)
