#innerloopsex8.py
# write a python program which will accept list of numerical values and display the prime numbers
lst=list()
nt=int(input("How Many Numbers  u Have:"))
if(nt<=0):
	print("{} is Invalid Input".format(nt))
else:
	for i in range(1,nt+1):
		val=int(input("Enter {} number:".format(i)))
		lst.append(val)
	else:
		print("-"*40)
		print("Given List of elements={}".format(lst)) # [12, 21, 3, 7, 14, 46]
		print("-"*40)
		primelist=list()
		nonprimelist=[]
		for n in lst:   #outer for loop--which will supply the values of list one by one
			if(n<=0):pass
			else:
				result=True
				for i in range(2,n):
					if(n%i==0):
						result=False
						break
				if(result):
					primelist.append(n)
				else:
					nonprimelist.append(n)
		else:
			print("Given List={}".format(lst))
			print("Prime Numbers List={}".format(primelist))
			print("Non-Prime Numbers List={}".format(nonprimelist))
