#Program for illustrating Polymorphism without inheritance and method overriding
#anotherpolyex1.py
class India:
	def  typecnt(self):
		print("\nIndia is developing country:")
	def  language(self):
		print("Indian speak Telugu, Hindi, English..many more lang")
	
class USA:
	def  typecnt(self):
		print("\nUSA is developed   country:")
	def  language(self):
		print("Americans speaks English")
	
class RSA:
	def  typecnt(self):
		print("\nRSA is developed   country:")
	def  language(self):
		print("Russia speaks Rssian Lang")

#main program
I=India()
U=USA()
R=RSA()
for obj in list( [I,U,R] ):  # here one object 'obj' contains reference of 3 objects and hence obj is polymorphism obj.
	obj.typecnt()
	obj.language()
	




