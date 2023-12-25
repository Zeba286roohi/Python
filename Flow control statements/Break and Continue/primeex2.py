#This program  accept a number and decide wethere it is prime or not
#primeex2.py
n=int(input("Enter a Number:"))
if(n<=1):
	print("{} is invalid input:".format(n))
else:
	result="Prime"
	for i in range(2,n):
		if(n%i==0):
			result="Not Prime"
			break
	
	if(result=="Prime"):
		print("{} is Prime:".format(n))
	else:
		print("{} is not Prime:".format(n))
