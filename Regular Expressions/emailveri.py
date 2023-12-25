#write a python program which will extract email id's from the given text
#emailveri.py
import re
text="Rossum mail id is rossum_12_psf@psf.com , ritche mail id is ritche_c@belllabs.co.in , Gosling mail id is  gosling_1_java@sun.net.org and Travis email id is travis_numpy@numpy.org  and kvr mail id is  kvr1.java@gmail.com . "
emails=re.findall("\S+@\S+", text)
for mail in emails:
	print("\t{}".format(mail))
