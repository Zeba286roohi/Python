#Menu driven application for arithmetic operations by using match case statement
#aop.py
import sys
print("-"*50)
print("\tArithmetic Operations")
print("-"*50)
print("\t1. Addition:")
print("\t2. Substraction:")
print("\t3. Multiplication:")
print("\t4. Division:")
print("\t5. Modulo Division:")
print("\t6. Exponetiation:")
print("\t7. Exit:")
print("-"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
	case 1: 
				a,b=float(input("Enter First Value for Addition:")),float(input("Enter Second Value for Addition:"))
				print("sum({},{})={}".format(a,b,a+b))
	case 2: 
				a=float(input("Enter First Value for Substraction:"))
				b=float(input("Enter Second Value for Substraction:"))
				print("sub({},{})={}".format(a,b,a-b))
	case 3: 
				a=float(input("Enter First Value for Multiplication:"))
				b=float(input("Enter Second Value for Multiplication:"))
				print("mul({},{})={}".format(a,b,a*b))
	case 4: 
				a=float(input("Enter First Value for Division:"))
				b=float(input("Enter Second Value for Division:"))
				print("div({},{})={}".format(a,b,a/b))
				print("floor div({},{})={}".format(a,b,a//b))
	case 5: 
				a=float(input("Enter First Value for Modulo Division:"))
				b=float(input("Enter Second Value for Modulo Division:"))
				print("mod({},{})={}".format(a,b,a%b))
	case 6: 
				a=float(input("Enter Base:"))
				b=float(input("Enter Power:"))
				print("exp({},{})={}".format(a,b,a**b))
	case 7: 
				print("\nThanks for Using Program!")
				sys.exit()
	case _:
				print("Ur Choice of selection is wrong!")


