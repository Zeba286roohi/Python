#reverse function

lst=[10,"Rossum",33.56,"Python","hyd"]
print(lst)
lst.reverse()
print(lst)

#sort function-sort in asc order
lst=[10,23,54,-3,-67,90,0,-43,89]
print(lst)
lst.sort()
print(lst)
#desc order printing
lst.reverse()
print(lst)
#printing strings
lst=["kiwi","apple","banana","orange","mango"]
print(lst)
lst.sort()
print(lst)
lst.reverse()
print(lst)

#sorting fun with rev bool with homogenous data
lst=[10,23,54,-3,-67,90,0,-43,89]
lst.sort(reverse=True)#desc order printing
print(lst)

lst=[10,23,54,-3,-67,90,0,-43,89]
lst.sort(reverse=False)#asc order printing
print(lst)

#Extend function-one list to another list obj
lst1=[10,20,30,40]
lst2=["python","java","cpp"]
#lst1.extend(lst2)
#print(lst1)
lst3=["Ds","Django","Numpy","pandas"]
print(lst3)
lst1.extend(lst2)
print(lst1)
lst1.extend(lst3)
print(lst1)
#extend list with + op
lst1=[10,20,30,40]
lst2=["python","java","cpp"]
lst3=["Ds","Django","Numpy","pandas"]
lst=lst1+lst2+lst3
print(lst)


