#breakex2.py
lst=[10,"Rossum",34.56,True,2+3j]
for val in lst:
	if(val==True):
		break
	else:
		print("\t{}".format(val))

