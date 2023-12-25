#This program takes list of values and extract only +ve values
#FilterEx2.py
def   positve(n):
	if n>0:
		return True
	else:
		return False

def  negative(n):
	if(n<0):
		return True
	else:
		return False
#main program
print("Enter list of values separated by space:")
lst=[int(val) for val in input().split()]
obj1=filter(positve,lst)
print("type of obj=",type(obj1)) #<class, 'filter'>
pslist=list(obj1)
print("Original Elements=",lst)
print("Possitive Elements=",pslist)
obj2=filter(negative,lst)
ngtpl=tuple(obj2)
print("Negative Elements=",ngtpl)