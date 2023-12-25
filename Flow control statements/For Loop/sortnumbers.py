#This Program accept number of Integer values and sort then in both ascending and decending orders
#sortnumbers.py
n=int(input("Enter How Many number u want sort:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	lst=list() # empty list
	print("Enter {} Values:".format(n))
	for i in range(1,n+1):
		val=int(input())
		lst.append(val)
	else:
		print("="*50)
		print("Original List of elements:")
		print("="*50)
		for val in lst:
			print("{}".format(val),end=" ")
		else:
			print()
			print("="*50)
			lst.sort() # lst data sorts in ascending order
			print("List of elements in Ascending Order:")
			for val in lst:
				print("{}".format(val),end=" ")
			else:
				print()
				print("="*50)
				lst.sort(reverse=True)
				print("List of elements in Decending Order:")
				for val in lst:
					print("{}".format(val),end=" ")
				else:
					print()
					print("="*50)



