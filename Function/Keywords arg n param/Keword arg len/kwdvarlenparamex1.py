#kwdvarlenparamex1.py
def dispinfo( **a): # here **a is called keyword variable length argrument / Parameter---dict
	print("-"*50)
	print("type of a=",type(a))
	print("No. of (Key,Value) ={}".format(len(a)))
	for k,v in a.items():
		print("\t{}--->{}".format(k,v))
	else:
		print("-"*50)


#main program
dispinfo(sno=10,sname="RS",marks=33.33,cname="PSF")
dispinfo(eno=111,ename="DR",sal=4.5)
dispinfo(crs1="Python1",crs2="Django")
dispinfo(author="Ritche")
dispinfo()


