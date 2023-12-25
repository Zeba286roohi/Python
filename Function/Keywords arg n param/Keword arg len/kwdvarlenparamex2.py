#This program computes total martks different student studying in different classes who secured in different subjects.
#kwdvarlenparamex2.py
def   findtotalmarks(sname,cls,**submarks):
	print("*"*50)
	print("\tS t u d e n t  M a r k s  R e p o r t:")
	print("*"*50)
	print("\tStudent Name:{}\tClass Name:{}".format(sname,cls))
	print("-"*50)
	tm=0
	print("\tSubject Name\tMarks")
	print("-"*50)
	for sub,marks in submarks.items():
		print("\t{}\t\t{}".format(sub,marks))
		tm=tm+marks
	else:
		print("-"*50)
		print("\tTotal Marks={}".format(tm))
		print("-"*50)
	print("*"*50)

#main program
findtotalmarks("Santosh","X",Sci=70,Soc=77,Maths=88,Hindi=55)
findtotalmarks("Umesh","XII",Maths=75,Phy=56,Che=55)
findtotalmarks("Venkatesh","B.Tech(Mech)",sub1=50,sub2=88,sub3=77,sub4=55)
findtotalmarks("Mahima","P.hD(DAA)", Core=90,Rm=56)
findtotalmarks("Rossum","Research")
