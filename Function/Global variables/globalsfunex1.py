#globalsfunex1.py
a=10
b=20
c=30
d=40   # here a,b,c,d are called global variables
def  operation():
	a=1
	b=2  # here 'a' and 'b' are called Local Variable
	print("val of a(global variable) in operation()=", globals().get('a'))
	print("val of b(global variable) in operation()=", globals()['b'] )
	print("val of a(Local Varaible) operation()=",a)
	print("val of b(Local Varaible) operation=",b)
	print("val of c (Global Variable) operation()=",c)
	print("val of d (Global variable) operation()=",d)

#main program
operation()
print("\nval of a main program=",a)
print("val of b main program=",b)
print("val of c main program=",c)
print("val of d main program=",d)
