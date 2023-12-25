#Program for  searching for files	
#searchfile.py
import os
try:
	foldername=input("Enter Folder Name:")
	listfiles=os.listdir(foldername)
	print("-"*50)
	print("Number of file in '{}' folder={}".format(foldername, len(listfiles)))
	print("-"*50)
	for filename in listfiles:
		print("\t{}".format(filename))
	print("-"*50)
	fname=input("Enter file name to search:")
	if (fname in listfiles):
		print("{} file  exists in {}".format(fname, foldername))
	else:
		print("{} file does not  exists in {}".format(fname, foldername))
except FileNotFoundError:
	print("Folders does not exists:")