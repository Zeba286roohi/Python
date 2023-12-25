#This Program accept a line of text and display the Vowels
#continueex4py
line=input("Enter a line of text:")  # Python is an oop lang
for v in line:
	if v not in ['a','e','i','o','u','A','E','I','O','U']:
		continue
	else:
		print("\t{} and whose index={}".format(v,line.index(v)))
