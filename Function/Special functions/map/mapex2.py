#This program accepts  list of elements and gets its square list.
#mapex2.py
print("Enter list of elements separated by space:")
oldlst=[int(val) for val in input().split()]
sqrlist=tuple(map(lambda val:val**2 , oldlst))
print("Original Elements:{}".format(oldlst))
print("New  Elements:{}".format(sqrlist))

