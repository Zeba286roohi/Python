#Write a python program which will accept a numerical
#positive integer value and decide weather it is prime or not
class Prime:
    def check(self,n):
        for i in range(2,n):
            if num%i==0:
                return 1
print("Enter a number:")
num=int(input())
obj=Prime()
s=obj.check(num)
if s==1:
    print("\n Number is not prime")
else:
    print("\n Number is Prime")
