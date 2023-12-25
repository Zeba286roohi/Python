#Program for accepting any number and obtains its reversed format
# Hint  : 1234------------> 4321
#palindrome.py
n=int(input("Enter a number:"))  # 1234
if(n<=0):
	print("{} is invalid input".format(n))
else:
	rn=0
	tn=n #preserver 'n' value into temp number 
	while(n>0):
		d=n%10
		rn=rn*10+d
		n=n//10
	else:
		if(rn==tn):
			print("Given Number is Palindrome:")
		else:
			print("Given Number is Not Palindrome:")

