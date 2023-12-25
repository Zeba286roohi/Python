#innerloopsex4.py
print("-"*40)
i=1
while(i<6):
	print("Val of i--outer while  loop=",i)
	print("-"*40)
	for j in range(1,4):
		print("\tVal of j-Inner for loop={}".format(j))
	else:
		i=i+1
		print("-"*40)
		print("i am out of inner for loop")
		print("-"*40)
else:
	print("i am out-of outer while loop")

"""
E:\KVR-PYTHON-9AM\INNER LOOPS>py innerloopsex4.py
----------------------------------------
Val of i--outer while  loop= 1
----------------------------------------
        Val of j-Inner for loop=1
        Val of j-Inner for loop=2
        Val of j-Inner for loop=3
----------------------------------------
i am out of inner for loop
----------------------------------------
Val of i--outer while  loop= 2
----------------------------------------
        Val of j-Inner for loop=1
        Val of j-Inner for loop=2
        Val of j-Inner for loop=3
----------------------------------------
i am out of inner for loop
----------------------------------------
Val of i--outer while  loop= 3
----------------------------------------
        Val of j-Inner for loop=1
        Val of j-Inner for loop=2
        Val of j-Inner for loop=3
----------------------------------------
i am out of inner for loop
----------------------------------------
Val of i--outer while  loop= 4
----------------------------------------
        Val of j-Inner for loop=1
        Val of j-Inner for loop=2
        Val of j-Inner for loop=3
----------------------------------------
i am out of inner for loop
----------------------------------------
Val of i--outer while  loop= 5
----------------------------------------
        Val of j-Inner for loop=1
        Val of j-Inner for loop=2
        Val of j-Inner for loop=3
----------------------------------------
i am out of inner for loop
----------------------------------------
i am out-of outer while loop"""