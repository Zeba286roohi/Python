#This program accepts  list of elements and gets its square list.
#mapex4.py
def   disp(lst):
	print("-"*40)
	for val in lst:
		print("%0.2f" %val)
	print("-"*40)

#mapex4.py
print("Enter list of elements separated by space:")
oldlst=[int(val) for val in input().split()]
sqrootlist=tuple(map(lambda val:val**0.5 , oldlst))
print("Original Elements:")
disp(oldlst)
print("New  Elements:")
disp(sqrootlist)

