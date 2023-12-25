#write a python program which will accept list of employees salaries between 1000 to any salary .
#give 15% hike to those employees who is drawing more than 5000  and give 30 % hike to those employees whose drawing less than 5000.
#mapex9.py
print("Enter List of Salaries of Employee:")
orginalsal=[int(sal) for sal in input().split()]
salless5000=list(filter(lambda sal:sal<=5000 ,orginalsal))
hikesallessthan5000=list(map(lambda sal:sal+sal*(30/100),salless5000 ))
salmore5000=list(filter(lambda sal:sal>5000,orginalsal))
hikesalmorethan5000=list(map(lambda sal:sal+sal*(15/100), salmore5000 ))
print("="*50)
print("\tSal Less Than 5000\t Hike Salaries")
print("="*50)
for sal,hsal in zip(salless5000,hikesallessthan5000):
	print("\t\t{}\t\t{}".format(sal,hsal))
print("="*50)
print("="*50)
print("\tSal More Than 5000\t Hike Salaries")
print("="*50)
for sal,hsal in zip(salmore5000,hikesalmorethan5000):
	print("\t\t{}\t\t{}".format(sal,hsal))
print("="*50)
