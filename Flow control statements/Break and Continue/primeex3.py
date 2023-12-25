#This program  accept a number and decide wethere it is prime or not
#primeex3.py
n=int(input("Enter a Number:"))
if(n<=1):
	print("{} is invalid input:".format(n))
else:
	result=0
	for i in range(2,n):
		if(n%i==0):
			result=1
			break
	#other statements
	if(result==0):
		print("{} is Prime:".format(n))
	else:
		print("{} is not Prime:".format(n))
