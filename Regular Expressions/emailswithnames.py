#emailswithnames.py
import re
text="Rossum mail id is rossum_12_psf@psf.com , Ritche mail id is ritche_c@belllabs.co.in , Gosling mail id is  gosling_1_java@sun.net.org and Travis email id is travis_numpy@numpy.org  and Kvr mail id is  kvr1.java@gmail.com . "
nameslist=re.findall("[A-Z][a-z]+",text) # Reg Expr for Names
mailslist=re.findall("\S+@\S+ ",text) # Reg Expr for mail-id extraction
print("-----------------------------------------------------------")
print("Name of Student\t\tMails of students:")
print("-----------------------------------------------------------")
for names,mails in zip(nameslist,mailslist):
	print("\t{}\t\t{}".format(names,mails))
print("---------------------------------------")