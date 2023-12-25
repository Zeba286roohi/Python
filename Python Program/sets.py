s={10,20,30,"xyz"}

s.update([88,99])
print(s)
print(type(s))
s.remove(30)
print(s)

f=frozenset(s)

#sets objects doesnot support indexing and slicing.




