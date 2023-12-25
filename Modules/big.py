#This program accept three numbers and file biggest amont them by using modules
#big.py---file name and treated as module name
def  big():
	a=int(input("Enter First value:"))
	b=int(input("Enter Second value:"))
	c=int(input("Enter Third value:"))
	if(a==b) and (b==c):
		print("ALL VALUES ARE EQUAL:")
	else:
		if(a>b) and (a>c):
			print("Biggest=",a)
		elif(b>c) and (b>a):
			print("Biggest=",b)
		else:
			print("Biggest=",c)
