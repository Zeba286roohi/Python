#Program for accepting 3 integers and find biggest among them
#bigex1.py
a=int(input("Enter First Number:"))  # 10
b=int(input("Enter Second Number:"))#b=13
c=int(input("Enter Third Number:"))# c=2
#find big
if(a>b) and (a>c):
	print("max({},{},{})={}".format(a,b,c,a))
elif(b>a) and (b>c):
	print("max({},{},{})={}".format(a,b,c,b))
elif(c>a) and (c>b):
	print("max({},{},{})={}".format(a,b,c,c))
elif(a==b) and (c==b) and (c==a):
	print("ALL Values are Equal:")