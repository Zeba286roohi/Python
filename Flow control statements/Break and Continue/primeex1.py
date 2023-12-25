#This program  accept a number and decide wethere it is prime or not
#primeex1.py
n=int(input("Enter a Number:"))
if(n<=1):
	print("{} is invalid input:".format(n))
else:
	result=True
	for i in range(2,n):
		if(n%i==0):
			result=False
			break
	
	if(result):
		print("{} is Prime:".format(n))
	else:
		print("{} is not Prime:".format(n))
