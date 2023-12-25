#WAP which will extract names of the students and their marks  which are present in the given text and 
#namesmarksex2.py
import re
studdata="Pranav is student  got marks 60 , Ankit is CEO  marks 99 , Santhosh is software eng and whose marks 65 , Ajay is reasearch student and marks 67 , Rossum is a developer got marks 35  and Mallesh is a teacher got 60  and Kuruva is data eng and got 77  and Manikanta is scientist got 88 and Umesh is a very good student got 79 ."
nameslist=re.findall("[A-Z][a-z]+",studdata) # Reg Expr for Names
markslist=re.findall("\d{2} ",studdata)
print("-----------------------------------------------------------")
print("Name of Student\t\tMarks of students:")
print("-----------------------------------------------------------")
for names,marks in zip(nameslist,markslist):
	print("\t{}\t\t{}".format(names,marks))
print("---------------------------------------")