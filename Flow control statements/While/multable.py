#This program generates mul table for a given +ve number
#multable.py
n=int(input("Ener a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	i=1
	print("*"*50)
	print("\tMul table for {}".format(n))
	print("*"*50)
	while(i<=10):
		print("\t{} x {}={}".format(n,i,n*i))
		i=i+1
	else:
		print("*"*50)
