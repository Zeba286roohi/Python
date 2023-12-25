#Phase-3: development of main program which will handle the exceptions
#multabledemo.py
from multable import table
from excepts import NegativeError,ZeroError
try:
	n=int(input("Enter a number:"))
	table(n)
except ValueError:
	print("\nDon't enter strs / alpha-numerics/symbols")
except NegativeError:
	print("\nDon't enter -ve numbers")
except ZeroError:
	print("\nDon't enter Zero :")

