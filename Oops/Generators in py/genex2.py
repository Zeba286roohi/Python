#genex2.py
def  kvrrange(l,u,s ):
	while(l<=u):
		yield l
		l=l+s

#main program
kr=kvrrange(10,21,2)
print("type of kr=",type(kr))
for i in kr:
	print(i)
