#program which will accept a number and decide whether it is even or odd.
num=int(input("Enter the number to check its even or odd:"))
if num%2==0:
    print("{}is even".format(num))
if num%2!=0:
    print("{} is odd".format(num))
