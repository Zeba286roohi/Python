#nonvarlenargex1.py----
#This program will not execute as it is shown bellow , bcoz PVM remebers latest function definition only.
def   dispvalues(a):
	print("{}".format(a))

def  dispvalues(a,b):
	print("{}\t{}".format(a,b))

def  dispvalues(a,b,c):
	print("{}\t{}\t{}".format(a,b,c))

def  dispvalues(a,b,c,d):
	print("{}\t{}\t{}\t{}".format(a,b,c,d))

#main program
dispvalues(10) # Function call-1
dispvalues(10,20) # Function call-2
dispvalues(10,20,30) # Function call-3
dispvalues(10,20,30,40) # Function call-4