#anonymousfunex1.py
def  addop(a,b):  # Normal Function Definition
	c=a+b
	return c

sumop=lambda a,b: a+b  # anonymous  Function definition

#main program
res=addop(10,20)
print("type of addop=",type(addop))# type of addop= <class 'function'>
print("sum=",res)
print("========================")
print("type of sumop=",type(sumop))  # type of sumop= <class 'function'>
x1=float(input("Enter First value:"))
x2=float(input("Enter Second value:"))
res1=sumop(x1,x2)
print("sum=",res1)