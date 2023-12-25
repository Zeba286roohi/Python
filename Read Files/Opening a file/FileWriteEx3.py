#This program demonstartes how write the data dynammically to the file by reading from KBD.
#FileWriteEx3.py
fname=input("Enter the file name to write the data:")
with open(fname,"a") as  fp:
	print("Enter the data and press '@' to stop:")
	while(True):
		kbddata=input()
		if(kbddata=="@"):
			break
		else:
			fp.write(kbddata+"\n")

	print("Data written to the file--verify")	