#This program reads the one line at a  from file ------readline()
#FileReadEx3.py
try:
	with open("addr1.data") as fp:
		fdata=fp.readline()
		print("File Data=",fdata)
		fdata=fp.readline()
		print("File Data=",fdata)
		fdata=fp.readline()
		print("File Data=",fdata)
		print("Index of fp=",fp.tell())

except FileNotFoundError:
	print("File does not exists:")
