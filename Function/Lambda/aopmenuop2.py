#Write a python program which will calculate all types of   academic operations (Use menu driven application along with anonymous function).
#aopmenuop2.py
# anonymous function definions
import sys
addop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divop=lambda a,b:a/b
floordivop=lambda k,v:k//v
modop=lambda k,v:k%v
expop=lambda k,v:k**v

def  aopmenu():  # Normal Function Definition
	print("="*50)
	print("\tA r i t h m e t i c  O p e r a t i o n s:")
	print("="*50)
	print("\t1.Addition:")
	print("\t2.Substraction")
	print("\t3.Multiplication")
	print("\t4.Division")
	print("\t5.Floor Division")
	print("\t6.Modulo Division")
	print("\t7.Exponentiation")
	print("\t8.Exit")
	print("="*50)

#main program
while(True):
	aopmenu()
	ch=int(input("Enter Ur Choice:"))
	match (ch):
		case 1: 
				x1=float(input("Enter First Value for Addition:"))
				x2=float(input("Enter Second Value for Addition:"))
				res=addop(x1,x2)
				print("Sum({},{})={}".format(x1,x2,res))
		case 2: 
				x1=float(input("Enter First Value for Substraction:"))
				x2=float(input("Enter Second Value for Substraction:"))
				res=subop(x1,x2)
				print("Sub({},{})={}".format(x1,x2,res))
		case 3: 
				x1=float(input("Enter First Value for Multiplication:"))
				x2=float(input("Enter Second Value for Multiplication:"))
				res=mulop(x1,x2)
				print("Mul({},{})={}".format(x1,x2,res))
		case 4: 
				x1=float(input("Enter First Value for Division:"))
				x2=float(input("Enter Second Value for Division:"))
				res=divop(x1,x2)
				print("Div({},{})={}".format(x1,x2,res))
		case 5: 
				x1=float(input("Enter First Value for Floor Division:"))
				x2=float(input("Enter Second Value for Floor Division:"))
				res=floordivop(x1,x2)
				print("FloorDiv({},{})={}".format(x1,x2,res))
		case 6: 
				x1=float(input("Enter First Value for Modulo Division:"))
				x2=float(input("Enter Second Value for Modulo Division:"))
				res=modop(x1,x2)
				print("Mod({},{})={}".format(x1,x2,res))
		case 7: 
				x1=float(input("Enter Base:"))
				x2=float(input("Enter Power:"))
				res=expop(x1,x2)
				print("expop({},{})={}".format(x1,x2,res))
		case 8: 
				print("Thanks for this program")
				sys.exit()
		case _: 
				print("Ur Selection of Operation is wrong!--try again")
			
	
