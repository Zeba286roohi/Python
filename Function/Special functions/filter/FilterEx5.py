#This program accepts list of values and extract Even Numbers
#FilterEx5.py
print("Enter list values separated by space:")
lst=[int(val) for val in input().split()]  # lst=[4 6 7 12 6 34 81]
evenlst=tuple(filter(lambda n : n%2==0,lst))
print("Original list=",lst)
print("Even list=",evenlst)
