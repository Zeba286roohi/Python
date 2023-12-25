#This program accepts  list of elements and gets its square list.
#mapex5.py
print("Enter list of elements separated by space:")
oldlst=[int(val) for val in input().split()]
sqrootlist=tuple(map(lambda val:val**0.5 , oldlst))
print("-"*50)
print("Original Elements\tSquare root Elements:")
print("-"*50)
for on,sn in zip(oldlst,sqrootlist):
	print("\t{}\t\t{}".format(on,round(sn,3)))
print("-"*50)
