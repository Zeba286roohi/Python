#Area of Triangle

a=float(input("Enter the first side"))
b=float(input("Enter the second side"))
c=float(input("Enter the third side"))

#calculate semi parimeter

s=(a+b+c)/2

#calculate the area

area=(s*(s-a)*(s-b)*(s-c))**0.5

print('the area of trianle is %0.2f' %area)
