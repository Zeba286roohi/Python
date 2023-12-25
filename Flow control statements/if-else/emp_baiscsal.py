#program to calculate net salary of employee based upon the following problem statements.
#accept Empno,Ename,and basic salary.if the basic salary is more than 10,000 give
#da=20% basicsal,ta=15%basicsal,hra=12%basicsal,cca=2%basicsal,gpf=2%baiscsal(deduction)
#lic=1%basicsal(deduction).

#Netsalary=(basicsal+da+ta+hra+cca+ma)-ArithmeticError(gpf+lic)

eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
basicsal=float(input("Enter Employee basic salary:"))
if(basicsal>=10000):
    da=(20/100)*basicsal
    ta=(15/100)*basicsal
    hra=(12/100)*basicsal
    cca=(2/100)*basicsal
    ma=(2/100)*basicsal
    gpf=(2/100)*basicsal
    lic=(1/100)*basicsal
else:
    da=(25/100)*basicsal
    ta=(20/100)*basicsal
    hra=(16/100)*basicsal
    cca=(3/100)*basicsal
    ma=(2/100)*basicsal
    gpf=(2/100)*basicsal
    lic=(1/100)*basicsal
netsal=(basicsal+da+ta+hra+cca+ma)-(gpf+lic)
print("Employee pay slip for the month of Fe2022")
print("-"*60)
print("Employee Number:{}".format(eno))
print("Employee Name:{}".format(ename))
print("Employee Basic Salary:{}".format(basicsal))
print("Employee DA:{}".format(da))
print("Employe TA:{}".format(ta))
print("Employee HRA:{}".format(hra))
print("Employee CCA:{}".format(cca))
print("Employee MA:{}".format(ma))
print("Employee GPF:{}".format(gpf))
print("Employee LIC:{}".format(lic))
print("-"*60)
print("Employee Net Salary:{}".format(netsal))
print("-"*60)
    
          





                                        
