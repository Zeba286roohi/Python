#This program accepts  list of elements and gets its square list.
#mapex1.py
def square(n):
	result=n**2
	return result

#main program
print("Enter list of elements separated by space:")
oldlst=[int(val) for val in input().split()]
mapobj=map(square,oldlst)
print("\nType of mapobj={}".format(type(mapobj)))
sqrlist=list(mapobj)
print("Original Elements:{}".format(oldlst))
print("New  Elements:{}".format(sqrlist))

