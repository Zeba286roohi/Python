#This program accepts list of values and find max and min from list of elements.
#reduceex3.py
from functools import reduce
print("Enter List of values separated by space:")
lst=[int(val) for val in input().split()]
big=reduce(lambda x,y: x if x>y else y, lst)
small=reduce(lambda x,y: x if x<y else y, lst)
print("\nList of elements={}".format(lst))
print("Biggest Element={}".format(big))
print("Smallest Element={}".format(small))
