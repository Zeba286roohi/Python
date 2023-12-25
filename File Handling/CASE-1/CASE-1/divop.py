#This Program accept two values from main program and computes their division
#divop.py------file name and acts as module name
from kvr import KvrDivisionError
def   division(a,b):
	if(b==0):
		raise KvrDivisionError  # Hitting or generating or raising an exception when cond is satisfied.
	else:
		return (a/b)


#Phase-2 :  Development of  Function which will hit programmer-defined exception with raise keyword