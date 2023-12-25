#WAP which will extract names of the students which are present in the given text
#namesex2.py
import re
studdata="Pranav is student , Ankit is CEO , Santhosh is software eng, Ajay is reasearch student, Rossum is a developer and Mallesh is a teacher and Kuruva is data eng and Manikanta is scientist  and Umesh is a very good student."
nameslist=re.findall("[A-Z][a-z]+ ", studdata)
print("--------------------------------------------------")
print("Names of Students in Ascending Order:")
print("--------------------------------------------------")
nameslist.sort()
for name in nameslist:
	print(name)
print("--------------------------------------------------")