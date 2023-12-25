#Program for  renaming a folder	
#renamedirex.py
import os
try:
	os.rename("c:\\mango","c:\\india")
	print("Folder renamed  successfully--verify")
except FileNotFoundError:
	print("Folders does not exists")
