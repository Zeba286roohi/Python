#globalkwdex3.py
a=10
b=20   # here 'a' and 'b' are called Global Variables
def   operation():
	global a,b
	a=a+1
	b=b+1

def  updatevalues():
	global a,b
	c=a*b
	print("Val of c in updatevalues()=",c)
	a=a+2
	b=b+2

#main program
print("Val of a before operation()=",a) # 10
print("Val of b before operation()=",b) # 20
operation()
print("Val of a after operation()=",a) # 11
print("Val of b after operation()=",b) # 21
updatevalues()
print("Val of a after updatevalues()=",a) # 13
print("Val of b after updatevalues()=",b) # 23
