#palindrome

i=int(input("Enter a number to check palindrome:"))
x=i
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i/10
if(x==rev):
     print("palindrome number:")
else:
    print("Not a palindrome:")
            
    
