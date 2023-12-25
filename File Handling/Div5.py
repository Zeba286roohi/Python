#program for cal division of two numbers
#Div5.py
try:
	print("\nI am try Block")
	s1=input("\nEnter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1)#--------------------------X
	b=int(s2) #-------------------------X
	c=a/b #------------------------------X
	s="PYTHON"
	print(s[0])
	x=int("10","20")
except ZeroDivisionError:
	print("\nDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\nDON'T ENTER strs / symbols / alpha-numeric strs")
except  IndexError :
	print("Plz Check ur Index")
except :
	print("OOOPs some thing went wrong!!!")
else:
	print("------else  block----")
	print("val of a=",a)
	print("val of b=",b)
	print("Div=",c)
finally:
	print("\ni am finally block")
