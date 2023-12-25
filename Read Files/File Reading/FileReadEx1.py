#This program reads the content of any file and displays on the console.----read()
#FileReadEx1.py
fname=input("Enter the file Name:")
try:
	with  open(fname,"r") as fp:
		filedata=fp.read()
		print("content of file:")
		print("-----------------------------------")
		print(filedata)
		print("-----------------------------------")
except FileNotFoundError:
	print("File does not exists:")