#This program takes list of values and extract only +ve values
#FilterEx3.py
positive=lambda x: x>0
negative=lambda k : k<0
#main program
print("Enter list of values separated by space:")
lst=[int(val) for val in input().split()]
pslist=list(filter(positive,lst))
nglist=tuple(filter(negative,lst))
print("---------------------------------------")
print("Original Elements=",lst)
print("Positive Elements=",pslist)
print("Negative Elements=",nglist)
print("---------------------------------------")



