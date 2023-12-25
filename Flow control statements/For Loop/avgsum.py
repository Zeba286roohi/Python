#Program accepting list of values and find sum and avg--Approach-1.
#avgsum.py
n=int(input("Enter How many elements sum u want to find:")) # 5
if(n<=0):
	print("{} is Invalid Input:".format(n))
else:
	i=1
	s=0
	while(i<=n):
		val=float(input("Enter {} Value:".format(i)))
		s=s+val
		i=i+1
	else:
		print("Sum={}".format(s))
		print("Average={}".format(s/n))
