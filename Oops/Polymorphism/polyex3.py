#WAP program which will calculate area of different figures by using classes and objects with polymorphism
#polyex3.py
class Circle:
	def  area(self): # original method
		self.r=float(input("Enter Radious:"))
		ac=3.14*self.r**2
		print("Area of Circle={}".format(ac))

class Rect:
	def area(self): # original method
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		ar=self.l*self.b
		print("Area of Rect={}".format(ar))
	
class Square(Rect,Circle):  # Multiple Inheritance
	def  area(self): # overridden method
		print("---------------------------------------------")
		self.s=float(input("Enter Side:"))
		sa=self.s**2
		print("Area of Square={}".format(sa))
		print("---------------------------------------------")
		Circle.area(self) # calling area() of Circle  from Square
		Rect.area(self) # calling area() of Rect  from Square
		
#main program
s=Square()
s.area()


