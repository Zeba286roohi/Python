#This program accepts two lists of elements and find their sum.
#mapex8.py
print("Enter list of elements for First List")
lst1=[float(val) for val in input().split()]
print("Enter list of elements for Second List")
lst2=[float(val) for val in input().split()]
sumlst=list(map(lambda x,y:x+y,lst1,lst2))
print("="*50)
print("\tList1\tList2\tList1+List2")
print("="*50)
for x,y,z in zip(lst1,lst2,sumlst):
	print("\t{}\t{}\t{}".format(x,y,z))
print("="*50)
