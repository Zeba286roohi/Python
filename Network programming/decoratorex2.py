#decoratorex2.py
def  square(kvr): 
	def   operation():
		n=kvr()
		res=n**2
		return res
	return operation

@square
def  getval():
	return (float(input("Enter a number:")))

#main program
result=getval()
print("result=",result)
