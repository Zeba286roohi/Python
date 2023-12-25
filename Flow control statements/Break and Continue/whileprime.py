n=int(input("Enter the number"))
count=0
i=2
while(i<=n//10):
    if(n%i==0):
        count=1
        break
    i=i+1
if(count==0):
    print("Number is prime")
else:
    print("Number is not prime")


