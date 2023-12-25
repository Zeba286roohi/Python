#This program accepts list of Srings  separated by comma  and obtain single line.
#reduceex4.py
import functools
print("Enter List of values separated by comma:")
lst=[ str(val)  for val in input().split(",")]
print("content of list=",lst)
singleline=functools.reduce(lambda x,y:x+" "+y,lst)
print("Result={}".format(singleline))