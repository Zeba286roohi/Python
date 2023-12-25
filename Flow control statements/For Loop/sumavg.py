#Program accepting list of values and find sum and avg--Approach-1.
#sumavg.py
n=int(input("Enter How many elements sum u want to find:")) # 5
if(n<=0):
	print("{} is Invalid Input:".format(n))
else:
	lst=list()    #  [ ]
	for i in range(1,n+1):
		val=float(input("Enter {} Value:".format(i)) )
		lst.append(val)
	else:
		print("-"*40)
		print("Content of list={}".format(lst))
		print("-"*40)
		s=0
		for val in lst:
			print("\t{}".format(val))
			s=s+val
		else:
			print("-"*50)
			print("\tsum={}".format(s))
			print("\tAvg={}".format(s/len(lst)))
			print("-"*50)
		
