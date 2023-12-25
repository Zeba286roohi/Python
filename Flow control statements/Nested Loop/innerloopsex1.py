#innerloopsex1.py
print("-"*40)
for i in range(1,6):
	print("Val of i-Outer loop={}".format(i))
	print("-"*40)
	for j in range(1,4):
		print("\tVal of j-Inner loop={}".format(j))
	else:
		print("-"*40)
		print("i am out of inner loop")
		print("-"*40)

else:
	print("I am out of outer for loop")
	print("-"*40)


"""
E:\KVR-PYTHON-9AM\INNER LOOPS>py innerloopsex1.py
----------------------------------------
Val of i-Outer loop=1
----------------------------------------
        Val of j-Inner loop=1
        Val of j-Inner loop=2
        Val of j-Inner loop=3
----------------------------------------
i am out of inner loop
----------------------------------------
Val of i-Outer loop=2
----------------------------------------
        Val of j-Inner loop=1
        Val of j-Inner loop=2
        Val of j-Inner loop=3
----------------------------------------
i am out of inner loop
----------------------------------------
Val of i-Outer loop=3
----------------------------------------
        Val of j-Inner loop=1
        Val of j-Inner loop=2
        Val of j-Inner loop=3
----------------------------------------
i am out of inner loop
----------------------------------------
Val of i-Outer loop=4
----------------------------------------
        Val of j-Inner loop=1
        Val of j-Inner loop=2
        Val of j-Inner loop=3
----------------------------------------
i am out of inner loop
----------------------------------------
Val of i-Outer loop=5
----------------------------------------
        Val of j-Inner loop=1
        Val of j-Inner loop=2
        Val of j-Inner loop=3
----------------------------------------
i am out of inner loop
----------------------------------------
I am out of outer for loop
----------------------------------------
"""