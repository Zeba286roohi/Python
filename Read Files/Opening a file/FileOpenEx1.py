#This program opens "kvr.data" in read mode
#FileOpenEx1.py
try:
	fp=open("kvr.data")  # Here fp is an object of TextIOWrapper
except FileNotFoundError:
	print("File does not exists")
else:
	print("\nFile Opened in read mode successfully")
	print("Type of fp=",type(fp))
	print("-"*40)
	print("File Mode=",fp.mode)
	print("is readable?=",fp.readable())
	print("is writeable?=",fp.writable())
	print("Is file Closed=",fp.closed)
	print("-"*40)
finally:
	print("i am from finally block")
	fp.close()  # manual Closing of files
	print("Is file Closed in finally block=",fp.closed)
