#This program accept list of values and sort them
#listsort.py
def disp(k):
	print("-"*40)
	for val in k:
		print("\t{}".format(val))
	else:
		print("-"*40)

def  sortelements(lst):
	print("Original Elements")
	disp(lst)
	lst.sort()
	print("Sorted Elements in Ascending Order")
	disp(lst)
	lst[::-1]   #  or  lst.reverse()      or  lst.sort(reverse=True)
	print("Sorted Elements in Decending Order")
	disp(lst)

#main program
lst=[10,2,222,50,10,4,55,-3,0,22]
sortelements(lst)
