def average(a,b):
    print("average of two number is",(a+b)/2)
average(10,20)
#printing prime
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))
