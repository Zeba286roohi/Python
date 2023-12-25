#RegExpr1.py
#Q)  find the word "Python" and no.of times repeated ---findall()
import re
givendata="Python is an OOP lang and Python is also Functional Programming Lang."
sp="Python"
mat=re.findall(sp,givendata) # mat is variable of type <class,'list'>
print("No. of occurences of '{}'={}".format(sp,len(mat)))

