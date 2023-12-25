#This program reads the specified number characters from file ------read(no. of chars)
#FileReadEx2.py
try:
	with open("addr1.data") as fp:
		print("Initial Position of fp=",fp.tell()) # 0
		fdata=fp.read(5)
		print("file data=",fdata)
		print("Now Position of fp=",fp.tell()) # 5
		fdata=fp.read(8)
		print("file data=",fdata)
		print("Now Position of fp=",fp.tell()) # 13
		fdata=fp.read()
		print("file data=",fdata)
		print("Now Position of fp=",fp.tell()) # 183
		fp.seek(0)  # Here fp repostioned to starting index
		print("--------------------------------------------")
		fdata=fp.read()
		print("file data=",fdata)
		print("--------------------------------------------")
except FileNotFoundError:
	print("File does not exists:")
