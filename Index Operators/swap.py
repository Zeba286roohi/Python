#program to accept any two values and swap them or interchange them using multiline assign

a=input("Enter value of a")
b=input("Enter value of b")
print("-"*50)
print("Original value of a:{}".format(a))
print("Original value of b:{}".format(b))
a,b=b,a
print("Swappped values of a:{}".format(a))
print("Swappped values of b:{}".format(b))