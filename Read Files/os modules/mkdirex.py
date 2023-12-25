#Program for  creating a folder	
#mkdirex.py
import os
try:
	os.mkdir("D:\\kiwi\mango\guava")
	print("Folder created successfully--verify")
except FileExistsError:
	print("Folder already exists")
except FileNotFoundError:
	print("Creation of Folders Hierarchy is not possible:")