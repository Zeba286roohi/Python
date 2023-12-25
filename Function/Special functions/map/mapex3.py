#This program accepts  list of elements and gets its square list.
#mapex3.py
print("Enter list of elements separated by space:")
oldlst=[int(val) for val in input().split()]
sqrootlist=tuple(map(lambda val:val**0.5 , oldlst))
print("Original Elements:{}".format(oldlst))
print("New  Elements:{}".format(sqrootlist))

