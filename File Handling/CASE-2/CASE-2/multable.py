#Phase-2: development of FUNCTION fe displaying result and hitting exceptions
#multable.py---file name and acts as module name
from excepts import NegativeError,ZeroError
def   table(n):
	if(n==0):
		raise ZeroError
	elif(n<0):
		raise NegativeError
	else:
		print("-"*40)
		print("Mul Table for {}".format(n))
		print("-"*40)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
		print("-"*40)