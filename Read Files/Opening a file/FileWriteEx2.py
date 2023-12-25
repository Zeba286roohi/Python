#This program demonstartes how write address of various people by using writelines()
#FileWriteEx2.py
d={"Name":"Rossum","HNO":"3-4-Hill Side","Cname":"PSF","country":"Nether Lands"}
with open("addr2.data","a") as fp:
	fp.writelines("\n"+str(d) )
	print("\nData Written to the file--plz verify:")