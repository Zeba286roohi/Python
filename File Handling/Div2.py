#program for cal division of two numbers
#Div2.py
try:
	print("\nI am try Block")
	s1=input("\nEnter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1)#--------------------------X
	b=int(s2) #-------------------------X
	c=a/b #------------------------------X
except ZeroDivisionError:
	print("\nDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\nDON'T ENTER strs / symbols / alpha-numeric strs")
else:
	print("------else  block----")
	print("val of a=",a)
	print("val of b=",b)
	print("Div=",c)
finally:
	print("\ni am finally block")
