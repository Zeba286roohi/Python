#This program demonstartes how write address of various people by using write()
#FileWriteEx1.py
with open("addr1.data","a") as fp:
	fp.write("Dennis Ritche\n")
	fp.write("5-4,Mountain side\n")
	fp.write("Bell Labs\n")
	fp.write("USA\n")
	print("\nData Written to the file--plz verify:")