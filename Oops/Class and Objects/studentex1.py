#This program stores stno,name and marks
#studentex1.py
class Student:pass  # here Student is called Programmer-defined data type



#main program
s=Student()     
print("content of s=",s.__dict__)  #  { }
print("Number of values in s=", len(s.__dict__))
