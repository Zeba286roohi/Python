# This program generates 1 to n numbers where 'n' is +ve 
#NumGenex1.py
n=int(input("Enter How many numbers number u want generate:"))
if(n<=0):
	print("{} is invalid input".format(n))
else:
	i=1 #Initlization part
	print("-"*50)
	print("Range of Values within:{}".format(n))
	print("-"*50)
	while(i<=n): # cond part
		print("Val of i=",i)
		i=i+1 #updation part
	else:
		print("-"*50)
		print("\nI am from else part of while loop")
	print("\ni am from other part of program")
	    