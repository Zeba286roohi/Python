#numgenex2.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("*"*50)
	print("Numbers within:{}".format(n))
	print("*"*50)
	for  i  in range(1,n+1):
		print("\t{}".format(i))
	print("*"*50)