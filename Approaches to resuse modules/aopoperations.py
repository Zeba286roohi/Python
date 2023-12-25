def addop():
    a=float(input("Enter First Value for addition:"))
    b = float(input("Enter Second Value for addition:"))
    print("sum({},{})={}".format(a,b,a+b))
def subop():
    a = float(input("Enter First Value for Substraction:"))
    b = float(input("Enter Second Value for Substraction:"))
    print("sub({},{})={}".format(a, b, a - b))
def mulop():
    k = float(input("Enter First Value for Multiplication:"))
    v = float(input("Enter Second Value for Multiplication:"))
    print("mul({},{})={}".format(k, v, k * v))
def divop():
    k = float(input("Enter First Value for Division:"))
    v = float(input("Enter Second Value for Division:"))
    print("Div({},{})={}".format(k, v, k / v))
    print("Floor Div({},{})={}".format(k, v, k // v))
def expop():
    k = float(input("Enter Base:"))
    v = float(input("Enter Power:"))
    print("pow({},{})={}".format(k, v, k ** v))
def modop():
    k = float(input("Enter First Value for Modulo Division:"))
    v = float(input("Enter Second Value for Modulo Division:"))
    print("Mod({},{})={}".format(k, v, k %v))

