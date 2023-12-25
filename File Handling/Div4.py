#program for cal division of two numbers
#Div4.py
try:
	print("\nI am try Block")
	s1=input("\nEnter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1)#--------------------------X
	b=int(s2) #-------------------------X
	c=a/b #------------------------------X
except ZeroDivisionError as k:
	print(k) # division by zero
except ValueError as v:
	print(v)  # invalid literal for int() with base 10: '10abc'
else:
	print("------else  block----")
	print("val of a=",a)
	print("val of b=",b)
	print("Div=",c)
finally:
	print("\ni am finally block")
