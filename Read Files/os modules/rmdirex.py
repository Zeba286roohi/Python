#Program for  removing a folder	
#rmdirex.py
import os
try:
	os.rmdir("D:\\hyd")
	print("Folder removed successfully--verify")
except FileNotFoundError:
	print("Specified Folders does not exists")
except OSError:
	print("Specified Folder is not empty--not possible to remove")