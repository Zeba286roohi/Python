#Program accepting list of values and find sum and avg--Approach-1.
#sumavg1.py
print("Enter Number of Values separated by space:")
lst=[float(val) for val in input().split()]  # List Comprehension
print("Content of list={}".format(lst))
s=0
for val in lst:
	print("\t{}".format(val))
	s=s+val
else:
	print("-"*50)
	print("\tsum={}".format(s))
	print("\tAvg={}".format(s/len(lst)))
	print("-"*50)
		
