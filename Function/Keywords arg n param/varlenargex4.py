#Write a python program which will compute sum of variable number of numerical values
#varlenargex4.py
def   findsum(sname,  *nums,crs="PYTHON",city="hyd"):
	print("="*50)
	print("My Name is '{}' doing '{}' course AND LIVING IN:{}".format(sname,crs,city))
	s=0
	for val in nums:
		print("\t{}".format(val))
		s=s+val
	else:
		print("sum={}".format(s))
		print("="*50)

#main program
findsum("Mahdev",10,20,30,40,50,60)
findsum("pooja",10,20)
findsum("supriya",10,20,30)
findsum("priyanka",12.3,34.5,5.6,-5.7)
findsum("venkatesh",1.2,13)
findsum("pavan",23,45,67,-56,78,12,-34,56)
findsum("nani")
#findsum(crs="Dajngo",sname="KVR",5,6,7)---SyntaxError: positional argument follows keyword argument
#findsum("KVR",5,6,7,,"Django") TypeError: unsupported operand type(s) for +: 'int' and 'str'
findsum("KVR",5,6,7,crs="Django")
findsum("Pranav",15,16,17,crs="Data Science",city="AP")
findsum("Ajay-Ankit",15,16,city="Delhi-BANG")
