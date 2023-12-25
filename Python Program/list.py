#list program
#Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to
#store collections of data
lst=[10,20,'zeba',-10,20,8]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))
lst.append(40)
#name will remove
lst.remove('zeba')
# 20 will go from here
del(lst[1])
print(lst)

#clear element
#lst.clear()
#print(lst)


#inserting number
print(max(lst))
print(min(lst))
lst.insert(3,99)
print(lst)
lst.insert(5,56)
print(lst)

#sorred in ascending order
lst.sort()
print(lst)

# Descending order
lst.sort(reverse=True)
print(lst)
