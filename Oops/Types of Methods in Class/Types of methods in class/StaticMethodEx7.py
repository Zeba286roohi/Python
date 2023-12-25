#This program accept two value and compute all aops
#StaticMethodEx7.py
class Aop:
	def  readvalues(self):
		self.a=float(input("Enter First Value:"))
		self.b=float(input("Enter Second Value:"))
		self.op=input("Enter Any Arithmetic Operator:")

class Calc:
	@staticmethod
	def  calculate(x): # x= {'a': 10.0, 'b': 20.0, 'op': '*'}
		match(x.op):
			case "+":
				print("sum({},{})={}".format(x.a,x.b,x.a+x.b))
			case "-":
				print("sub({},{})={}".format(x.a,x.b,x.a-x.b))
			case "*":
				print("mul({},{})={}".format(x.a,x.b,x.a*x.b))
			case "/":
				print("Div({},{})={}".format(x.a,x.b,x.a/x.b))
			case "//":
				print("Floor Div({},{})={}".format(x.a,x.b,x.a//x.b))
			case "**":
				print("exp({},{})={}".format(x.a,x.b,x.a**x.b))
			case "%":
				print("mod({},{})={}".format(x.a,x.b,x.a%x.b))
			case _:
				print("{} is not a Arithmetic Operator:".format(x.op))

#main program
ao=Aop()
ao.readvalues()
#call static method and pass 'ao' object
Calc.calculate(ao)