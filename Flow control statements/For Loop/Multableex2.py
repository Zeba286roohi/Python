#Multableex2.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-"*50)
	print("Mul table for {}".format(n))
	print("-"*50)
	for  i  in range(1,11):
		print("\t{} x {}={}".format(n,i,n*i))
	else:
		print("-"*50)
