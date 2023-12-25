#iteratorex1.py
lst=[10,20,30,40,50,60,70,80]  # Iterable objects
print(lst)
for x in lst:
	print(x)
print("==========================")
iterobj=iter(lst)  # here iterobj is an object of Iterator
while(True):
	try:
		print(next(iterobj))
	except StopIteration:
		break