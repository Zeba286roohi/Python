#genex3.py
import sys
def  kvrrange(l,u,s ):
	if(l>u):
		print("Invalid Input")
		sys.exit()
	else:
		while(l<=u):
			yield l
			l=l+s

#main program
lb=int(input("Enter Lower Bound Value:"))
ub=int(input("Enter upper Bound Value:"))
s=int(input("Enter Step Value:"))
kr=kvrrange(lb,ub,s)
print("="*50)
while(True):
	try:
		print(next(kr))
	except StopIteration:
		print("="*50)
		break