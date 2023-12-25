#Program for  listing files	
#listfiles.py
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
except FileNotFoundError:
	print("Folders does not exists:")