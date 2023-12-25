#mobilenumbervalidation.py
import re
while(True):
	mno=input("Enter ur mobile number:")#12345678ab
	if(len(mno)==10):
		result=re.search("\d{10}",mno)
		if(result!=None):
			print("Ur Mobile Number is Valid")
			break
		else:
			print("Mobile Number should not contain Alphabets / special symbols")
	else:
		print("Mobile Number must contain 10 digits:")


