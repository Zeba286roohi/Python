#nondecorator.py
def  getval():
	return (float(input("Enter a number:")))

def   square():
	n=getval()
	return n**2

def cube():
	n=square()
	return n**3
#main program
res=cube()
print("Result=",res)

