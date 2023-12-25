#emppayslip.py
eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
basicsal=float(input("Enter Employee Basic Salary:"))
if(basicsal>=10000):
	da= (20/100)*basicsal
	ta=(15/100)*basicsal
	hra=(12/100)*basicsal
	cca=(2/100)*basicsal
	ma=(2/100)*basicsal
	gpf=(2/100)*basicsal #  deduction
	lic=(1/100)*basicsal   # deduction
else:
	da= (25/100)*basicsal
	ta=(20/100)*basicsal
	hra=(16/100)*basicsal
	cca=(3/100)*basicsal
	ma=(2/100)*basicsal
	gpf=(2/100)*basicsal #  deduction
	lic=(1/100)*basicsal   # deduction
netsal=(basicsal+da+ta+hra+cca+ma)-(gpf+lic)
#display the pay slip
print("-"*60)
print("\tEmployee Pay Slip for the Month of Feb-2022")
print("-"*60)
print("\tEmployee Number:{}".format(eno))
print("\tEmployee Name:{}".format(ename))
print("\tEmployee Basic salary:{}".format(basicsal))
print("\tEmployee DA:{}".format(da))
print("\tEmployee TA:{}".format(ta))
print("\tEmployee HRA:{}".format(hra))
print("\tEmployee CCA:{}".format(cca))
print("\tEmployee MA:{}".format(ma))
print("\tEmployee GPF:{}".format(gpf))
print("\tEmployee LIC:{}".format(lic))
print("-"*60)
print("\tEmployee Net Salary:{}".format(netsal))
print("-"*60)