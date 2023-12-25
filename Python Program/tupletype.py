# Tuple  cannot be modiefed if once created.It maintain the insertion order.paranthesis is optional.

tpl=(40,50,40,'xyz')
print(tpl)
print(tpl[3])
#slicing or repeating 3 times
print(tpl*3)
print(tpl.count(40))
print(tpl.index('xyz'))

#definig list here,list always define with square bracket

lst=[67,12,'abc']
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
print(tpl1)




