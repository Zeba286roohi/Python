#program which will accept any numerical integer value and display even no with init.
n=int(input("Enter the number its even no:"))
if(n<=0):
    print("{}invalid input".format(n))
else:
    i=2
    print("="*50)
    print("Even numbers are {}".format(n))
    while(i<=n):
        print("{}".format(i))
        i=i+2
        
   
    
              
