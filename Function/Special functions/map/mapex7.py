#This program accepts  list of Old Salaries of employees and gets new salary list
#mapex7.py
print("Enter list of old slaries  of employees:")
oldsal=[float(val) for val in input().split()]
newsal=list(map(lambda sal:sal+sal*0.15,oldsal))
print("="*50)
print("Old Salaries \t New Salaries")
print("="*50)
for old,new in zip(oldsal,newsal):
	print("\t{}\t{}".format(old,round(new,3)))
print("="*50)
