#kwdparamex1.py
def disp(a,b,c):
	print("\t{}\t{}\t{}".format(a,b,c))

#main program
print("="*50)
print("\ta\tb\tc")
print("="*50)
disp(10,20,30)
disp(c=30,b=20,a=10)
disp(b=30,a=10,c=20)
disp(10,c=30,b=20)
disp(10,20,c=30)
#disp(c=30,10,20)-----error---SyntaxError: positional argument follows keyword argument
print("="*50)
