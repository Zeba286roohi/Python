#WAP program which will calculate area of different figures by using classes and objects with polymorphism
#polyex4.py
class Circle:
	def  area(self,r): # original method
		ac=3.14*r**2
		print("Area of Circle={}".format(ac))

class Square:  
	def  area(self,s): # original method 
		print("---------------------------------------------")
		sa=s**2
		print("Area of Square={}".format(sa))
		print("---------------------------------------------")
		
class Rect(Square,Circle): # multiple Inheritance
	def area(self,l,b): # overridden method
		ar=l*b
		print("Area of Rect={}".format(ar))
		super().area(12)
		Circle.area(self,1.5)
	
#main program
l=float(input("Enter Length:"))
b=float(input("Enter Breadth:"))
r=Rect()
r.area(l,b)


