#WAP program which will calculate area of different figures by using classes and objects with polymorphism
#ployex2.py
class Circle:
	def  area(self): # original method
		self.r=float(input("Enter Radious:"))
		ac=3.14*self.r**2
		print("Area of Circle={}".format(ac))

class Rect(Circle):
	def area(self): # overridden method
		self.l=float(input("Enter Length:"))
		self.b=float(input("Enter Breadth:"))
		ar=self.l*self.b
		print("Area of Rect={}".format(ar))
		super().area()
		
class Square(Rect):
	def  area(self): # overridden method
		super().area()
		self.s=float(input("Enter Side:"))
		sa=self.s**2
		print("Area of Square={}".format(sa))
	
#main program
s=Square()
s.area()


