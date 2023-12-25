n=int(input("Enter the number:"))
a=0
b=1
count=0
if(n<=0):
    print("Invalid integer")
else:
    while(count<=n):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
        count=count+1
