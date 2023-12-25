#abstractclass2.py
class Operations:
	def  perform(self,a,b):pass   # null body method

class Rect(Operations):
	def  perform(self,a,b):  # Overriding null body methods
		self.ar=a*b
		print("Area of Rect={}".format(self.ar))

class Swap(Operations):
	def perform(self,a,b):  #Overriding null body methods
		print("Original Value of a:{}".format(a))
		print("Original Value of b:{}".format(b))
		b,a=a,b # multi line assignment
		print("Swapped Value of a:{}".format(a))
		print("Swapped Value of b:{}".format(b))

#main program
r=Rect()
r.perform( float(input("Enter Length:")),float(input("EnterBreadth:")) )
print("="*50)
s=Swap()
s.perform( input("Enter First Value:"), input("Enter Second Value:") ) 