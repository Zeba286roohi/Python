def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

#main pro
num=int(input("Enter the number:"))
if num<0:
    print("Sorry negative numbers are not accepted:")
elif num==0:
    print("Fact of 0 is 1")
else:
    print("Fact of number is ",fact(num))
