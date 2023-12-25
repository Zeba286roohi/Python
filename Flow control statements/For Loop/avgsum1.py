#Program accepting list of values and find sum and avg--Approach-1.
#avgsum1.py
n=int(input("Enter How many elements sum u want to find:")) # 5
if(n<=0):
	print("{} is Invalid Input:".format(n))
else:
	i=1
	s=0
	print("Enter {} Values:".format(n))
	while(i<=n):
		val=float(input())
		s=s+val
		i=i+1
	else:
		print("Sum={}".format(s))
		print("Average={}".format(s/n))
