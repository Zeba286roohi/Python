#innerloopsex6.py
# write a python program which will accept list of numerical values and display the multiplication table for every value of list.
lst=list()
nt=int(input("How Many mul tables u want:"))
if(nt<=0):
	print("{} is Invalid Input".format(nt))
else:
	for i in range(1,nt+1):
		val=int(input("Enter {} number:".format(i)))
		lst.append(val)
	else:
		print("-"*40)
		print("Given List of elements={}".format(lst))
		print("-"*40)
		for n in lst:  # Outer for loop
			if(n<=0):
				print("{} is invalid input and No Mul Table:".format(n))
			else:
				print("-"*40)
				print("Mul Table for {}".format(n))
				print("-"*40)
				for i in range(1,11):  # inner for loop
					print("\t{} x {}={}".format(n,i,n*i))
				else:
					print("-"*40)


