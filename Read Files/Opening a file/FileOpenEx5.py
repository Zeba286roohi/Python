#This program demonstartes various file opening modes with "with open() as " as approach
#FileOpenEx5.py
try:
	with open("hyd1.info","x") as fp:
		print("-"*50)
		print("Name of file=",fp.name)
		print("File Mode=",fp.mode)
		print("is file readable=",fp.readable())
		print("is file wrietable=",fp.writable())
		print("Is file closed in with open()=",fp.closed)
		print("-"*50)
except FileExistsError:
	print("File already exists--it can't create again")
else:
	print("\ni am out of with open() indentation--else block:")
	print("Is file closed in with open()=",fp.closed)

