def decimal_binary(decimal_1):
    decimal=int(decimal_1)
    print("The given decimal number",decimal,"in binary number is",bin(decimal))

def decimal_octal(decimal_1):
    decimal=int(decimal_1)
    print("The given decimal number",decimal,"in octal number is",oct(decimal_1))

def decimal_hexa(decimal_1):
    decimal=int(decimal_1)
    print("The given decimal nunber",decimal,"in hexa number is",hex(decimal_1))

#main pro
decimal_1=int(input("Enter the number:"))
decimal_binary(decimal_1)
decimal_octal(decimal_1)
decimal_hexa(decimal_1)


