n=int(input("Enter a number"))
if(n<=0):
    print("Invalid Input",n)
else:
    i=1
    print("-"*40)
    print("Multiplication table of",n)
    while(i<=10):
        print(n,"x",i,"=",n*i)
        i=i+1
    else:
        print("*"*50)
