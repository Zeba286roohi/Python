#This program display the values of list,tuple,set, dict
#iterabledisp.py
def disp(k):
	print("type of k=",type(k))
	print("-"*40)
	for val in k:
		print("\t{}".format(val))
	else:
		print("-"*40)

def   dispdict(k):
	print("type of k=",type(k))
	print("-"*40)
	for cno,cname in k.items():
		print("\t{}-->{}".format(cno,cname))
	else:
		print("-"*40)

#main program
lst=[10,20,30,40,50]
disp(lst) #function call
tpl=("Python","Django","Data Science","ML","DL")
disp(tpl)  #function call
s={10,"Rossum",34.56,"Python",True}
disp(s)  #function call
d={1:"Python",2:"Data Science",3:"Django",4:"Java",5:".Net"}
dispdict(d) # function call