#This program takes list of values and extract only +ve values
#FilterEx1.py
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
lst=[10,-20,30,0,40,-50,-60,70,23]
obj1=filter(positve,lst)
print("type of obj=",type(obj1)) #<class, 'filter'>
pslist=list(obj1)
print("Original Elements=",lst)
print("Possitive Elements=",pslist)
obj2=filter(negative,lst)
ngtpl=tuple(obj2)
print("Negative Elements=",ngtpl)