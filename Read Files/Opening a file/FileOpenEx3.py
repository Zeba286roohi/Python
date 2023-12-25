#This program demonstartes various file opening modes with "with open() as " as approach
#FileOpenEx3.py
try:
	with open("hyd.info","r+") as fp:
		print("-"*50)
		print("Name of file=",fp.name)
		print("File Mode=",fp.mode)
		print("is file readable=",fp.readable())
		print("is file wrietable=",fp.writable())
		print("Is file closed in with open()=",fp.closed)
		print("-"*50)
except FileNotFoundError:
	print("File does not exists")
else:
	print("Is file closed in with open() in else block=",fp.closed)
