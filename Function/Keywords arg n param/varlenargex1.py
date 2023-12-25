#varlenargex1.py
def   dispvalues(*a):  # here *a is called variable argument and whose type is tuple
	print("="*50)
	print("\ntype of a:{} and length={}".format(type(a), len(a)))
	for val in a:
		print("\t{}".format(val))
	else:
		print("="*50)



#main program
dispvalues(10) # Function call-1
dispvalues(10,20) # Function call-2
dispvalues(10,20,30) # Function call-3
dispvalues(10,20,30,40) # Function call-4
dispvalues("RS","DR","MC","TR","SS") # Function call-5