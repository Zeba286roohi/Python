#program which will read which accepts numerical integer value and decide whether it is
#positive negative or zero.

num=float(input("Enter the number to check it is positive and Negative:"))
if num>0:
    print("{}is positive".format(num))
if num<0:
    print("{}is Negative".format(num))
if num==0:
    print("{}is Zero".format(num))
    
