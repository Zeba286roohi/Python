def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
   return x/y

def power(x,y):
     return pow(x,y)
print("select operation")
print("1.add")
print("2.sub")
print("3.mult")
print("4.div")
print("5.power")
choice=input("Enter the choice(1/2/3/4/5):")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if choice=='1':
         print(num1,"+",num2,'=',add(num1,num2))
if choice=='2':
         print(num1,"-",num2,'=',sub(num1,num2))

if choice=='3':
         print(num1,"*",num2,'=',mult(num1,num2))
if choice=='4':
         print(num1,"/",num2,'=',div(num1,num2))
if choice=='5':
         print(num1,"^",num2,'=',power(num1,num2))
else:
 print("Result")
            
    
