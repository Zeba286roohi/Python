#innerloopsex2.py
print("-"*40)
i=1
while(i<6):
	print("Val of i--outer while  loop=",i)
	print("-"*40)
	j=1
	while(j<4):
		print("\tVal of j-inner  while loop=",j)
		j=j+1
	else:
		print("-"*40)
		print("\ti am out-of inner  while loop")
		i=i+1
		print("-"*40)
else:
	print("i am out-of outer while loop")


"""
E:\KVR-PYTHON-9AM\INNER LOOPS>py innerloopsex2.py
----------------------------------------
Val of i--outer while  loop= 1
----------------------------------------
        Val of j-inner  while loop= 1
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 3
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i--outer while  loop= 2
----------------------------------------
        Val of j-inner  while loop= 1
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 3
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i--outer while  loop= 3
----------------------------------------
        Val of j-inner  while loop= 1
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 3
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i--outer while  loop= 4
----------------------------------------
        Val of j-inner  while loop= 1
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 3
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
Val of i--outer while  loop= 5
----------------------------------------
        Val of j-inner  while loop= 1
        Val of j-inner  while loop= 2
        Val of j-inner  while loop= 3
----------------------------------------
        i am out-of inner  while loop
----------------------------------------
i am out-of outer while loop"""