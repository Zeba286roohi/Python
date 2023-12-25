#write  python program which will generate multiplication table for a given number by using modules concept
#multable.py-----file name and module name
def table():
	n=int(input("Enter a number:"))
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		print("="*50)
		print("Mul Table for {}".format(n))
		print("="*50)
		for i in range(1,11):
			print("\t{} x {}={}".format(n,i,n*i))
		else:
			print("="*50)


