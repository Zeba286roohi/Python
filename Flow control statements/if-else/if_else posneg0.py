#program which will accept a numerical integer value and decides whether it is positive negative or zero

n=int(input("Enter a number to check number is positive negative or zero:"))
if n>0:
    print("{}is Positive".format(n))
else:
    if n<0:
        print("{}is Negative".format(n))
    else:
        print("{} is zero".format(n))
    
