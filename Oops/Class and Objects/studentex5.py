#This program stores stno,name and marks
#studentex5.py
class Student:  # here Student is called Programmer-defined data type
	crs="PYTHON"  # here crs is called Class Level Data members 

#main program
s1=Student()     
s2=Student()     
print("Content of s1 before adding the data=",s1.__dict__)
print("Content of s2 before adding the data=",s2.__dict__)
print("-"*50)
#add the data to s1
print("Enter First Student Information")
print("-"*50)
s1.sno=int(input("Enter Student Number:"))
s1.sname=input("Enter Student Name:")
s1.marks=float(input("Enter Student Marks:"))    # here sno,sname and marks are called Instance data members
#add the data to s2
print("Enter Second Student Information")
print("-"*50)
s2.sno=int(input("Enter Student Number:"))
s2.sname=input("Enter Student Name:")
s2.marks=float(input("Enter Student Marks:"))    # here sno,sname and marks are called Instance data members
print("-"*50)
print("First Student Information:")
print("-"*50)
print("Student Number=",s1.sno)
print("Student Name=",s1.sname)
print("Student Marks=",s1.marks)
print("Student Course=",Student.crs) # accessing Class Level Data Members w.r.t Class Name
print("-"*50)
print("Second Student Information:")
print("-"*50)
print("Student Number=",s2.sno)
print("Student Name=",s2.sname)
print("Student Marks=",s2.marks)
print("Student Course=",Student.crs) # accessing Class Level Data Members w.r.t Class Name
print("-"*50)
