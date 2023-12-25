#sets
s1={10,10,10,10}
print(s1,type(s1))#did not maintain duplicates

l1=[10,10,10,10,10,10,10]
print(l1,type(l1))#maintain duplicate


#Add()
s1={10,"Rossum"}
print(s1,type(s1),id(s1))
s1.add("Python")
s1.add(15.89)
print(s1,type(s1),id(s1))

s1.add("Zeba")
print(s1,type(s1),id(s1))

s2=set()
s2.add(100)
s2.add(300)
s2.add("Django")
print(s2,type(s2),id(s2))


#Clear()
s1={10,"Python","Rossum",45,67.3,True,2+4j}
print(s1,type(s1))
len(s1)
s1.clear()
print(s1,type(s1))
len(s1)

#Copy():used to copy one setobj to another setobji,e implemnting shallow copy
s1={10,"Python","Rossum",45,67.3,True,2+4j}
print(s1,type(s1),id(s1))
s2=s1.copy()
print(s2,type(s2),id(s2))
s1.add("Java")
s2.add("Django")
print(s1,type(s1),id(s1))
s1={10,"Python","Rossum",45,67.3,True,2+4j}
print(s1,type(s1),id(s1))
s2=s1
print(s2,type(s2),id(s2))
s1.add("Django")
print(s1,type(s1),id(s1))
print(s2,type(s2),id(s2))

#Remove():
s1={10,"Rossum","Python"}
l=[10,20,30,40]
t=(10,20,30,40)
s1.add(t)
print(s1,type(s1),id(s1))
s2={"DT","ML","AI"}
s1.add(s2)
t1=(10,"KVR",(10,20,30),"IOUCET")
print(t1)
l1=[10,"KVR",(10,20,30),"IOUCET"]#inside set list can b possible
print(l1)

#remove()
s1={10,"Python","Rossum",45,67.3}
print(s1)
s1.remove("Python")
print(s1)




      



