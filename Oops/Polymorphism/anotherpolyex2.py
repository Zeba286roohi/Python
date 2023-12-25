#Program for illustrating Polymorphism without inheritance and method overriding
#anotherpolyex2.py
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

class CountryInfor:
	@staticmethod
	def  disp(obj):   #  This displays multiple object information and this method is Polymorphic 
		                                                  #Method.
		obj.typecnt()
		obj.language()


#main program
I=India()
U=USA()
R=RSA()
#pass I , U and R object disp() of CountryInfor class
CountryInfor.disp(I)
CountryInfor.disp(U)
CountryInfor.disp(R)

	
	




