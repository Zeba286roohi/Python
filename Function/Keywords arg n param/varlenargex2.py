#varlenargex2.py
def   dispvalues(*a):
	for val in a:
		print("{}".format(val),end=" ")
	else:
		print()

#main program
print("="*50)
dispvalues(10) # Function call-1
dispvalues(10,20) # Function call-2
dispvalues(10,20,30) # Function call-3
dispvalues(10,20,30,40) # Function call-4
dispvalues("RS","DR","MC","TR","SS") # Function call-5
print("="*50)