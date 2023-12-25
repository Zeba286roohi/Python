#globalvarex3.py
def   learnDataSci():
	crs1="Data Science" # crs1 is called local variable
	print(" To do coding in '{}' , we need '{}' language:".format(crs1,lang))
	#print(crs2,crs3) can't access crs2 and crs3 bcoz they are local in other functions
lang="PYTHON"  # here 'lang' is called Global Variable
def   learnAI():
	crs2="AI" # crs2 is called local variable
	print(" To do coding in '{}' , we need '{}' language:".format(crs2,lang))
	#print(crs1,crs3) can't access crs1 and crs3 bcoz they are local in other functions

def   learnML():
	crs3="ML" # crs3 is called local variable
	print(" To do coding in '{}' , we need '{}' language:".format(crs3,lang))
	#print(crs1,crs2) can't access crs1 and crs2 bcoz they are local in other functions
#main program
learnDataSci()
learnAI()
learnML()