#Type casting techniques

a=10.24
print(a,type(a))
b=int(a)
print(b,type(b))

a=0.99
print(a,type(a))
b=int(a)
print(b,type(b))

#bool to int
a=True
print(a,type(a))
b=int(a)
print(b,type(b))


a=False
print(a,type(a))
b=int(a)
print(b,type(b))

#complex to int
'''
a=2+5j
print(a,type(a))
b=int(a)
print(b,type(b))
gives error'''

#str to int
a="100"
print(a,type(a))
'a=a+1 not possible'
b=int(a)
print(b,type(b))
b=b+1
print(b,type(b))

a="12.3" #float str
print(a,type(a))
'b=int(a) val err'

a=True
print(a,type(a))
b=float(a)
print(b,type(b))

a=2+3j
print(a,type(a))
'b=float(a) not possible as it a j'

a="123"
print(a,type(a))
b=float(a)
print(b,type(b))

#int to bool(if no is non zero returns true else false)
a=123
print(a,type(a))
b=bool(a)
print(b,type(b))
a=0
print(a,type(a))
b=bool(a)
print(b,type(b))

a=0.0
print(a,type(a))
b=bool(a)
print(b,type(b))

#complex to bool
a=2+3j
print(a,type(a))
b=bool(a)
print(b,type(b))

a=0+0j
print(a,type(a))
b=bool(a)
print(b,type(b))

a="123"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="12.34"
print(a,type(a))
b=bool(a)
print(b,type(b))

a="0"
print(a,type(a))
b=bool(a)
print(b,type(b))
print(len(a))



