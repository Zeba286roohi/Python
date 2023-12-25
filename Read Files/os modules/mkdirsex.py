#Program for  creating a folders Hierarchy	
#mkdirsex.py
import os
try:
	os.makedirs("D:\\India\Hyd\Ameerpet\Python\Data Science")
	print("Folders created successfully--verify")
except FileExistsError:
	print("Folder already exists")
