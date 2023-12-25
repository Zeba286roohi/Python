#calculate cube root of n

n=int(input("Enter the n th root:"))
m=int(input("Enter the m th root:"))

cube=n**(1/3)
root=m**(1/3)
print("*"*40)
print("The cube root is {}={}".format(n,cube))
print("*"*40)
print("The mth root is {}={}".format(m,root))
