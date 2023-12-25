#RegExpr3.py
#Q)  find the word "Python" and no.of times repeated --finditer()
import re
givendata="Python is an OOP lang and Python is also Functional Programming Lang."
sp="python".title()
noc=0
mat=re.finditer(sp,givendata) # mat is variable of type <class,'list'>
print("---------------------------------------------------")
print("Matching Results:")
print("---------------------------------------------------")
for m in mat:   # here 'm' is an object of <class 're.Match'>
	print("\nStart Index={}  End Index={}   Value={}".format(m.start(),m.end(),m.group()))
	noc=noc+1
print("---------------------------------------------------")
print("Number of Occurences of '{}'={}".format(sp,noc))
print("---------------------------------------------------")
