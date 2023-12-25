#genex1.py
def  kvrrange(l,u ):
	while(l<=u):
		yield l
		l=l+1


#main program
kr=kvrrange(10,21)
print("type of kr=",type(kr))
for i in kr:
	print(i)