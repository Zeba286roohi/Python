#Indexex.py
line=input("Enter a line of text:")
print("Given Data={}".format(line))
for ch in line:
	print("\tCharacter: {}   Index={}".format(ch,line.find(ch)))