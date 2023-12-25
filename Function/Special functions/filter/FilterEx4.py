#This program takes list of values and extract only +ve values
#FilterEx4.py
print("Enter list of values separated by space:")
lst=[int(val) for val in input().split()]
pslist=list(filter(lambda x: x>0,lst))
nglist=tuple(filter(lambda k : k<0,lst))
print("---------------------------------------")
print("Original Elements=",lst)
print("Positive Elements=",pslist)
print("Negative Elements=",nglist)
print("---------------------------------------")



