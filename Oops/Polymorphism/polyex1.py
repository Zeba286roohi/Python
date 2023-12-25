#polyex1.py
class Circle(object):
	def draw(self): # Original Method
		print("Drawing Circle--Circle Class")
		#super().draw()---------------invalid, bcoz object class does not contain draw()

class Rect(Circle):
	def draw(self):   # Overridden Method
		print("Drawing--Rect--Rect Class")
		super().draw() # will draw() of Circle Class from draw() of Rect class

class Square(Rect):
	def  draw(self):  # Overridden Method
		print("Drawing--Square--Square Class")
		super().draw() # will draw() of Rect Class from draw() of Square class

#main program
s=Square()
s.draw()