#program to calculate simple interest and total amount to pay
#SI=PTR/100
print("Enter Principal amount:")
p=float(input())
print("Enter Rate of Interest:")
r=float(input())
print("Enter Time Period:")
t=float(input())
si=p*t*r/100
print("Simple interest is={}".format(si))
#total amout to pay total=p+si
total=p+si
print("Total amount to pay is={}".format(total))
