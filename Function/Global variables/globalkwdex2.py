#globalkwdex2.py
a=10
def  increment():
	global a
	a=a+1
	print("val of a in fun1()=",a) # 11

def multiplyval():
	global a
	a=a*2
	print("val of a in multiplyval()=",a) #22
#main program
print("Val of a in main program before increment()=",a) # 10
increment()
print("Val of a in main program after increment()=",a) # 11
multiplyval()
print("Val of a in main program after multiplyval()=",a) # 22
