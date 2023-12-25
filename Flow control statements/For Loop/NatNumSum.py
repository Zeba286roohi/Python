#NatNumSum.py
n=int(input("Enter a number for finding sum of First Numbers , squares and cubes:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	s,ss,cs=0,0,0
	print("-"*50)
	print("\tNat Nums\tSquares\t\tCubes")
	print("-"*50)
	for val in range(1,n+1):
		print("\t{}\t\t{}\t\t{}".format(val, val**2,val**3))
		s=s+val
		ss=ss+val**2
		cs=cs+val**3
	else:
		print("-"*50)
		print("\t{}\t\t{}\t\t{}".format(s,ss,cs))
		print("-"*50)

