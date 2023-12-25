#Program for cal simple int by using modules and Packages
#sim.py----File Name and acts as module name
def    simpleint():
	p=float(input("Enter Principle Amount:"))
	t=float(input("Enter Time:"))
	r=float(input("Enter Rate of Interest:"))
	si=(p*t*r)/100
	totamt=p+si
	print("="*50)
	print("Principle Amount:{}".format(p))
	print("Time :{}".format(t))
	print("Rate of Intrest:{}".format(r))
	print("-"*50)
	print("Simple Interest={}".format(si))
	print("Total Amout to Pay={}".format(totamt))
	print("="*50)