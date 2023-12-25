#This program demonstartes various file opening modes with "with open() as " as approach
#FileOpenEx4.py
with open("hyd.info","a+") as fp:
	print("-"*50)
	print("Name of file=",fp.name)
	print("File Mode=",fp.mode)
	print("is file readable=",fp.readable())
	print("is file wrietable=",fp.writable())
	print("Is file closed in with open()=",fp.closed)
	print("-"*50)
print("\ni am out of with open() indentation:")
print("Is file closed in with open()=",fp.closed)
