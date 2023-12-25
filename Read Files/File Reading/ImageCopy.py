#This program copy the image of one file into another file 
#ImageCopy.py
sfile=input("Enter the source File which contains image:")
try:
	with open(sfile,"rb") as rp:
		dfile=input("Enter Destination File for placing:")
		with open(dfile,"wb") as wp:
			sfdata=rp.read()
			wp.write(sfdata)
			print("\n{}  File  Image  Copied into {}".format(sfile,dfile))
except FileNotFoundError:
	print("File does not exists")
