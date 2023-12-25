#fabonnic series :1,1,2,3,5,8,13,21,34

n=int(input("How many terms you want to print"))
n1=0
n2=1
count=2
if n<=0:
    print("enter the positive number")
elif n==1:
    print("Fabonacci sequence")
    print(n1)
else:
    print("Fabonnaic series")
    print(n1,",",n2,end=',')
    while count<n:
        res=n1+n2
        print(res,end=',')
        n1=n2
        n2=res
        count+=1
        
    
      
