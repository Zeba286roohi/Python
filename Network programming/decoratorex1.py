#decoratorex1.py
def  square(kvr): 
	def   operation():
		n=kvr()
		res=n**2
		return res
	return operation


def  getval():
	return 5

#main program
result=square(getval)
print("result=",result())
