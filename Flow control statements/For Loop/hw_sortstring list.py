#program to accept list of name and sort them in both ascending and descing orders.

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()

print("Element After Sorting List in Ascending Order is : ", NumList)
