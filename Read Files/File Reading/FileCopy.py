#This program copy the content of one file into another file 
#FileCopy.py
sfile=input("Enter the source File:")
try:
	with open(sfile,"r") as rp:
		dfile=input("Enter Destination File:")
		with open(dfile,"a") as wp:
			sfdata=rp.read()
			wp.write(sfdata)
			print("\n{}  File Data Copied into {}".format(sfile,dfile))
except FileNotFoundError:
	print("File does not exists")
