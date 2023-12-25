#This program accept any file name and find number of lines, words and characters .
#FileCountInfo.py
fname=input("Enter File Name:")
try:
	nol=0
	nw=0
	nc=0
	with open(fname,"r") as fp:
		Filelines=fp.readlines()
		for line in Filelines:
			print("{}".format(line),end="")
			nol=nol+1
			nw=nw+len(line.split())
			nc=nc+len(line)
		else:
			print("\n------------------------------------------")
			print("Number of lines=",nol)
			print("Number of words=",nw)
			print("Number of Characters=",nc)
			print("------------------------------------------")
except FileNotFoundError:
	print("File does not exists:")	