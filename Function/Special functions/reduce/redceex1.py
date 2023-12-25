#This program accepts list of values and find their sum by using reduce()
#redceex1.py
import functools
print("Enter List of values separated by space:")
lst=[int(val) for val in input().split()]
result=functools.reduce(lambda a,b:a+b,lst)
print("\nList of elements=",lst)
print("Sum=",result)




