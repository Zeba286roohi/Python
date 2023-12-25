#innerloopsex5.py
# write a python program which will accept list of numerical values and display the multiplication table for every value of list.

lst=[-3,6,-12,-19,-4,0]
for n in lst:
	if(n<=0):
		print("{} is invalid input and No Mul Table:".format(n))
	else:
		print("-"*40)
		print("Mul Table for {}".format(n))
		print("-"*40)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		else:
			print("-"*40)


