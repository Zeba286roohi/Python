#identity check with py 3.7 editor

a={10,20,30,40}
a=100
id(a)
a=None
b=None
a is b
#if two dict obj containing the same value is op is false is not is true
d1={10:"Apple",20:"Kiwis"}
d2={10:"Apple",20:"Kiwis"}
d1 is d2
print(id(d2))

s1={10,20,30}

s2={10,20,30}
print(id(s1))
s1 is s2
s1 is not s2
fs1=frozenset(s1)
fs2=frozenset(s2)
print(id(fs1))
print(id(fs2))

l1=[10,"Rosuum","Python"]
l2=[10,"Rossum","Python"]
l1 is l2
l1 is not l2
t1=tuple(l1)
t2=tuple(l2)
print(id(t1))
print(id(t2))
t1 is t2
t1 is not t2
#range
r1=range(10,20)
r2=range(10,20)
print(id(r1))
print(id(r2))
r1 is r2
r1 is not r2
#Bytes
b1=bytes([10,20,30,40])
b2=bytes([10,20,30,40])
print(id(b1))
print(id(b2))
b1 is b2
b1 is not b2
ba1=bytearray([10,20,30,40])
ba2=bytearray([10,20,30,40])
print(id(ba1))
print(id(ba2))
ba1 is ba2
ba1 is not ba2

#str
s1="india"
s2="india"
print(id(s1))
print(id(s2))
s1 is s2
s1 is not s2
s1 is s3
s1 is not s3

#complex
a=2+3j
b=2+3j
a is b
#bool
a=True
b=True
a is b
a is not b

a,b=300,300
print(id(a))
print(id(b))
a,b=-10,-10
a is not b
a is b






