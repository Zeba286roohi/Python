#innerloopsex3.py
print("-"*40)
for i in range(1,6):  # outer loop
	print("Val of i-Outer for loop={}".format(i))
	print("-"*40)
	j=3
	while(j>0):  # Inner loop
		print("\tVal of j-inner  while loop=",j)
		j=j-1
	else:
		print("-"*40)
		print("\ti am out-of inner  while loop")
		print("-"*40)
else:
	print("I am out of outer for loop")
	print("-"*40)

"""
E:\KVR-PYTHON-9AM\INNER LOOPS>py innerloopsex3.py
----------------------------------------
Val of i-Outer for loop=1
----------------------------------------
        Val of j-inner  while loop= 3
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 1
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i-Outer for loop=2
----------------------------------------
        Val of j-inner  while loop= 3
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 1
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i-Outer for loop=3
----------------------------------------
        Val of j-inner  while loop= 3
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 1
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i-Outer for loop=4
----------------------------------------
        Val of j-inner  while loop= 3
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 1
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i-Outer for loop=5
----------------------------------------
        Val of j-inner  while loop= 3
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 1
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
I am out of outer for loop
----------------------------------------"""