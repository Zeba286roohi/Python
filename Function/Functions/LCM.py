def cal_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0)and (greater%y==0):
            lcm=greater
            break
        greater=greater+1
    return lcm

#main pro
num1=int(input("Enter the number:"))
num2=int(input("Enter the second number:"))
print("The lcm of",num1,"and",num2,"is:",cal_lcm(num1,num2))
