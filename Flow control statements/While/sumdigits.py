#This program accpets a number and find its digits
#sumdigits.py
n=int(input("Enter a number:"))
if(n<=0):
	print("{} is inavlid input".format(n))
else:
	print("-"*50)
	print("Given Number={}".format(n))
	print("-"*50)
	s=0
	while(n>0):
		d=n%10
		s=s+d
		n=n//10
	else:
		print("-"*50)
		print("Sum of digits={}".format(s))
		print("-"*50)	
