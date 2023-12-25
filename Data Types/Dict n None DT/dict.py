#dict item():
d={"Ts":"Hyd","kar":"Ban","tamil":"che"}
keyval=d.items()
print(keyval)
#dict_items([('Ts','hyd'),('kar','ban'),('tamil','che')])
for kv in keyval:
    print(kv)
for k,v in keyval:
    print(k ,"---->",v)

#dict update():
d1={10:3.4,20:4.5,30:6.7,40:3.4}
print(d1)
d2={100:1.2,200:2.2}
print(d2)
d1.update(d2)
print(d1)
d3={10:12.3,200:13.4}
print(d3)
d3.update(d1)
print(d3)



d1.update(d3)
print(d1)#d1 val is updated with d1 10 val changed here
d4={20:12.4,300:6.7}
print(d4)
d1.update(d4)
print(d1)
#delete
d1.pop(20)
#pop item remove last ie=tem
d1.popitem()
d1={1:["PY","ML","DL","AI"],2:["C","CPP",8086],3:["Java","Spring"]}
print(d1)
for k in d1.keys():
    print(k)

for v in d1.values():
    print(v)





          












