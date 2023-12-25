#Program for accepting any number and obtains its reversed format
# Hint  : 1234------------> 4321
#reverse.py
n=int(input("Enter a number:"))  # 1234
if(n<=0):
	print("{} is invalid input".format(n))
else:
	rn=0
	while(n>0):
		d=n%10
		rn=rn*10+d
		n=n//10
	else:
		print("Orginal Number={}".format(n))
		print("Reversed Number={}".format(rn))
	
