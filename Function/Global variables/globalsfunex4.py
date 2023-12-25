#globalsfunex4.py
a=10
b=20
c=30
d=40   # here a,b,c,d are called global variables
def  operation():
	global c,d;
	c=c+1  #  c= 31
	d=d+1 # 41
	a=1
	b=2  # here 'a' and 'b' are called Local Variable
	res=a+b+c+d
	print("result=",res)

#main program
operation()
