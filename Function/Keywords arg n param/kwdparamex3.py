#kwdparamex3.py
def  studinfo(sno,sname,marks,crs="Python"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("="*50)
print("\tstno\tName\tMarks\tCrs")
print("="*50)
studinfo(10,"RS",77.77)
studinfo(20,marks=22.22,sname="DR")
studinfo(marks=42.22,sno=30,sname="DR")
studinfo(crs="Django",marks=11.11,sname="TR",sno=40)
#studinfo(crs="Django",50,"MC",44.44) SyntaxError: positional argument follows keyword argument
print("="*50)
