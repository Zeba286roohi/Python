#This program accepts list of values and find max and min from list of elements.
#reduceex2.py
import functools
print("Enter List of values separated by space:")
lst=[int(val) for val in input().split()]
big=functools.reduce(lambda x,y: x if x>y else y, lst)
small=functools.reduce(lambda x,y: x if x<y else y, lst)
print("\nList of elements={}".format(lst))
print("Biggest Element={}".format(big))
print("Smallest Element={}".format(small))
