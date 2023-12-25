#progam to accept two inegers values and compute all assign op using multiline assign
#multi line assignment
a,b=float(input("Enter first value:")),float(input("Enter second value:"))
sum,sub,multi,div=a+b,a-b,a*b,a/b
print("addition:{} substraction;{} multiplication:{} dividion:{}".format(sum,sub,multi,div))

#swaping logic
a,b=10,12
print("Print a,b:{} {}".format(a,b))
a,b=b,a
print("swaping a,b: {} {}".format(a,b))
