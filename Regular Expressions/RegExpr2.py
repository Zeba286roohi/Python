#RegExpr2.py
#Q)  find the word "Python" and no.of times repeated --finditer()
import re
givendata="Python is an OOP lang and Python is also Functional Programming Lang."
sp="Python"
mat=re.finditer(sp,givendata) 
print("type of mat=",type(mat)) #  type of mat= <class 'callable_iterator'>
print("---------------------------------------------------")
print("Matching Results:")
print("---------------------------------------------------")
for m in mat:   # here 'm' is an object of <class 're.Match'>
	print("\nStart Index={}  End Index={}   Value={}".format(m.start(),m.end(),m.group()))
print("---------------------------------------------------")

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr2.py
type of mat= <class 'callable_iterator'>
---------------------------------------------------
Matching Results:
---------------------------------------------------

Start Index=0  End Index=6   Value=Python

Start Index=26  End Index=32   Value=Python
--------------------------------------------------- 

"""