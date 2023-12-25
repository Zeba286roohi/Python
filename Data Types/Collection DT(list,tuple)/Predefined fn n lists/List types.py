#append operation
l1=[10,"Rossum"]
print(l1,type(l1),id(l1))
l1.append(23.45)
print(l1,type(l1),id(l1))
#appending elements to empty list
l2=[]
print(l2,type(l2),id(l2))
l2.append(100)
l2.append("Rossum")
l2.append("Python")
print(l2,type(l2))

l1=[10,20,30,40]
l2=[10,"Rossum"]
l2.append(l1)
print(l2,type(l2))

#Insert Operation

l1=[10,"Rossum",34.56]
print(l1,type(l1))
#inserting elements in specified position here it is adding at 2 position
l1.insert(2,"Python")
print(l1,type(l1))


#Remove function it will not remove duplicate ele
l1=[10,20,30,50,"Rossum","py",20]
print(l1)
l1.remove(10)
print(l1)
l1.remove(20)
print(l1)

#pop(index) function del particular elem with index val
l1=[10,20,30,10,30,50,40,20,10]
print(l1)
l1.pop(3)

print(l1)
l1.pop(-1)
print(l1)

#pop function del last ele of list obj
l1=[10,20,"python",43.67,2+3j]
print(l1)
l1.pop()
print(l1)
l1.insert(2,"Java")
l1.pop()
print(l1)

#clear function removes all ele
l1=[10,20,"python",43.67,2+3j]
len(l1)
print(l1)
l1.clear()
print(l1)
len(l1)
#deleting ele
l1=[10,20,30,10,30,50,40,20,10]
print(l1)
del(l1[1:3])
print(l1)

#count is used to count no of occurance
l1=[10,20,30,10,30,50,40,20,10]
print(l1)
l1.count(20)
print(l1)

#copy(shallow copy) where memory address are diff
l1=[10,"Rossum"]
print(l1,id(l1))
l2=l1.copy()
print(l2,id(l2))

#deep copy
l1=[10,"Rossum"]
print(l1,id(l1))
l2=l1 #deep copy
print(l2,id(l2))

      
      









      
