#This program reads the all lines at a time  from file ------readlines()
#FileReadEx4.py
try:
	with open("addr1.data") as fp:
		lines=fp.readlines()
		print("----------------------------------------")
		print("File Data:")
		print("----------------------------------------")
		for line in lines:
			print("{}".format(line),end="")
		print("----------------------------------------")
except FileNotFoundError:
	print("File does not exists:")
