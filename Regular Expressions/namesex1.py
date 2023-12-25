#WAP which will extract names of the students which are present in the given text
#namesex1.py
import re
studdata="Pranav is student , Ankit is CEO , Santhosh is software eng, Ajay is reasearch student, Rossum is a developer and Mallesh is a teacher and Kuruva is data eng and Manikanta is scientist  and Umesh is a very good student."
nameslist=re.finditer("[A-Z][a-z]+ ", studdata)
print("--------------------------------------------------")
print("Names of Students:")
print("--------------------------------------------------")
for na in nameslist:
	print(na.group())
print("--------------------------------------------------")




