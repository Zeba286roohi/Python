#write a python program which will accept a line of text and separate them with vowels and consonents and special symbols
#alhabets.py
line=input("Enter a line of text:") # a3$b56hq3rt$#P"
vs=[]
cs=[]
ds=[]
ss=[]
for ch in line:
	if ch in ['a','e','i','o','u','A','E','I','O','U']:
		vs.append(ch)
	elif( ch  not in ['a','e','i','o','u','A','E','I','O','U'] and ch.isalpha()   ):
		cs.append(ch)
	elif( ch  not in ['a','e','i','o','u','A','E','I','O','U'] and ch.isdigit()   ):
		ds.append(ch)
	else:
		ss.append(ch)
else:
	print("--------------------------------------------")
	print("Given Line={}".format(line))
	print("Vowels List={}".format(vs))
	print("Cons. List={}".format(cs))
	print("Digits List={}".format(ds))
	print("Special Symbols List={}".format(ss))
	print("--------------------------------------------")


	




