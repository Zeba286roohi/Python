s1={10,20,30,40}
s2={10,40,50,60}
s3=s1.symmetric_difference(s2)
print(s3)
s4=s1^s2
print(s4)

#program which accept two numericals integers values and swap them using bitwise xor

a=int(input("Enter the value of a:"))
b=int(input("Enter value of b:"))
print("-"*40)
print("original value of a={}".format(a))
print("original value of b={}".format(b))
print("-"*40)
a=a^b
b=a^b
a=a^b
print("Swapped value of a={}".format(a))
print("Swapped value of b={}".format(b))


      
