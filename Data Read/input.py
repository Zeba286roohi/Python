print("Enter first val")
a=input()
print("Enter second val")
b=input()
print("val of a={} and its type={}".format(a,type(a)))
print("val of b={} and its type={}".format(b,type(b)))
'c=a*b'
'print("val of c={}".format(c,type(c)))'#gives err
#convert in to int or float
x1=float(a)
x2=float(b)
print("val of a={} and its type={}".format(x1,type(x1)))
print("val of b={} and its type={}".format(x2,type(x2)))
x3=x1*x2
print("val of x3{}= and its type={}".format(x3,type(x3)))


#mulex5
print("Enter two values")
a=int(input())
b=int(input())
c=a*b
print("mul({},{})={}".format(a,b,c))
#or
print("Enter two values")
print("mul={}".format(float(a)*float(b)))
