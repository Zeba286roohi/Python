#WAP which will read the text data from file which contains multiple student names and the marks and extract names and marks from thr given file
#namesmarksex3.py
import re
try:
	with open("D:\\ampt\\studinfo.data","r") as fp:
		filedata=fp.read()
		nameslist=re.findall("[A-Z][a-z]+",filedata) # Reg Expr for Names
		markslist=re.findall("\d{2} ",filedata) # # Reg Expr for Marks
		print("-----------------------------------------------------------")
		print("Name of Student\t\tMarks of students:")
		print("-----------------------------------------------------------")
		for names,marks in zip(nameslist,markslist):
			print("\t{}\t\t{}".format(names,marks))
		print("---------------------------------------")

except FileNotFoundError:
	print("File does not exists")