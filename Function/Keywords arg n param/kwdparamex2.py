#kwdparamex2.py
def disp(a,b,c,crs="PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(a,b,c,crs))

#main program
print("="*50)
print("\ta\tb\tc\tcrs")
print("="*50)
disp(10,20,30)
disp(c=30,b=20,a=10)
disp(b=20,a=10,c=30)
disp(10,c=30,b=20)
disp(10,20,c=30)
#disp(c=30,10,20)-----error---SyntaxError: positional argument follows keyword argument
disp(c=30,a=10,b=20)
disp(crs="Java",c=30,a=10,b=20)
#disp(10,20,crs="DSC",30) -----error---SyntaxError: positional argument follows keyword argument
disp(10,20,30,crs="JAVA")
disp(10,20,30,"Django")
print("="*50)
