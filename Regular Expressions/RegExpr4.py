#RegExpr4.py
#Q)  find the word "Python" and no.of times repeated --finditer()
import re
givendata="Java is an OOP lang and Python is also Functional Programming Lang and Python is used in AI."
sp="lang1"
mat=re.search(sp,givendata) 
print("type of mat=",type(mat)) # here mat is an object of <class 're.Match'> if match occurs other it returns <class,"NoneType">
if(mat!=None):
	print("\nSearch is Sucessful")
	print("Start Index={} and End Index={} and Value={}".format(mat.start(),mat.end(),mat.group()))
else:
	print("\nSearch is Un-Sucessful")
	print("'{}' does not exists in given data".format(sp))
