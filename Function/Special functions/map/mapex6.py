#This program accepts  list of elements and gets its square list and square root .
#mapex6.py
print("Enter list of elements separated by space:")
oldlst=[int(val) for val in input().split()]
sqrootlist=tuple(map(lambda val:val**0.5 , oldlst))
sqlist=tuple(map(lambda val:val**2 , oldlst))
print("-"*50)
print("Original\tSquareRoot\tSquare:")
print("-"*50)
for on,sqrtno,sqrno in zip(oldlst,sqrootlist,sqlist):
	print("\t{}\t{}\t\t{}".format(on,round(sqrtno,2),sqrno))
print("-"*50)
