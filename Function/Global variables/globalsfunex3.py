#globalsfunex3.py
a=10
b=20
c=30
d=40
def   operation():
	d=globals()
	print("------------------------------------------------------------")
	print("Out Function / Program Global variable Values:")
	print("------------------------------------------------------------")
	print("\tValue a =",d['a'] )
	print("\tValue b =",d['b'] )
	print("\tValue c =",d['c'] )
	print("\tValue d =",d['d'] )
	print("-----------------OR-----------------------------------------")
	print("\tValue a =",d.get('a') )
	print("\tValue b =",d.get('b') )
	print("\tValue c =",d.get('c') )
	print("\tValue d =",d.get('d') )
	print("-----------------OR-----------------------------------------")
	print("\tValue a =",globals().get('a'))
	print("\tValue b =",globals().get('b') )
	print("\tValue c =",globals().get('c') )
	print("\tValue d =",globals().get('d') )
	print("------------------OR----------------------------------------")
	print("\tValue a =",globals()['a'] )
	print("\tValue b =",globals()['b'] )
	print("\tValue c =",globals()['c'] )
	print("\tValue d =",globals()['d'] )


#main program
operation()
