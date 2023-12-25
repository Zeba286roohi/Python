#dictionary

dict1={1:"john",2:"bob",3:"bill"}
print(dict1)

k=dict1.keys()
for i in k:
    print(i)

#print value

v=dict1.values()
for i in v:print(i)
print(dict1[3])

#del

del dict1[2]
print(dict1)
