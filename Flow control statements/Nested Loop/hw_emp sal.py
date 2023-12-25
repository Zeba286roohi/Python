#program which will accepts employee number,employee name,and basic salary.
#Basic salary range from(1000 and 10,000)
#if the basic salary lies between 1000 and 5000 then give hra=15%basicsal
sno=int(input("Enter the Employee no:"))
sname=input("Enter the Name of the Employee:")
ssal=int(input("Salary of the employee is:"))
if(ssal>=10000):
    da=(20/100)*ssal
    ta=(15/100)*ssal
    hra=(12/100)*ssal
    cca=(2/100)*ssal
    ma=(2/100)*ssal
    gpa=(2/100)*ssal
    lic=(1/100)*ssal
else:
    da=(25/100)*ssal
    ta=(20/100)*ssal
    hra=(16/100)*ssal
    cca=(3/100)*ssal
    ma=(3/100)*ssal
    gpa=(2/100)*ssal
    lic=(1/100)*ssal
netsal=(ssal+da+ta+hra+cca+ma)-(gpa+lic)
print("="*60)
print("{} Sno of the employee".format(sno))
print("{} Name of the employee".format(sname))
print("="*50)
print("{} Basic Salary of the employee".format(ssal))
print("{} DA of the employee ".format(da))
print("{} TA of the employee".format(ta))
print("{} HRA of the employee".format(hra))
print("{} CCA of the employee".format(cca))
print("{} MA of the employee".format(ma))
print("{} GPA of the employee".format(gpa))
print("{} LIC of the employee".format(lic))
print("="*50)
print("{} Net salary of the employee".format(netsal))

    
