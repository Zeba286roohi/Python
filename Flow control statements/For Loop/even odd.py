#program which accept any integer values and generate even nos and odd nos seperately.
n=int(input("Enter the number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Even Numbers with in:{}".format(n))
    print("-"*50)
    for even in range(2,n+1,2):
        print("\t{}".format(even))
    else:
        print("odd nos with in:{}".format(n))
        for odd in range(1,n+1,2):
            print("\t{}".format(odd))
        
        
        
