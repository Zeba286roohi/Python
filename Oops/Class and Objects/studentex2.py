#This program stores stno,name and marks
#studentex2.py
class Student:pass  # here Student is called Programmer-defined data type

#main program
s1=Student()     
s2=Student()     
print("Content of s1 before adding the data=",s1.__dict__)
print("Content of s2 before adding the data=",s2.__dict__)
print("-"*50)
#add the data to s1
s1.sno=100
s1.sname="RS"
s1.marks=22.22    # here sno,sname and marks are called Instance data members
#add the data to s2
s2.sno=101
s2.sname="TR"
s2.marks=33.33     # here sno,sname and marks are called Instance data members
print("Content of s1 after adding the data=",s1.__dict__)
print("Content of s2 after adding the data=",s2.__dict__)


