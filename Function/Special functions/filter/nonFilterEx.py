#This program takes list of values and extract only +ve values
#nonFilterEx.py
def positivenegative(lst):
	pslist=[]
	nglist=[]
	for val in lst:
		if (val>0):
			pslist.append(val)
		else:
			nglist.append(val)
	return pslist,nglist

#main program
print("Enter list of values separated by space:")
lst=[int(val) for val in input().split()]
psl,ngl=positivenegative(lst)
print("Orginal Elements:",lst)
print("Possitive Elements:",psl)
print("Negetive Elements:",ngl)