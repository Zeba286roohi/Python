#iteratorex2.py
s="Python"
for x in s:
	print(x)
print("==========================")
iterobj=iter(s)  # here iterobj is an object of Iterator
print(type(iterobj))
while(True):
	try:
		print(next(iterobj))
	except StopIteration:
		break