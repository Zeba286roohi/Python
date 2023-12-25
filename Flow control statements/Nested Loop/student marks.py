#program which accept student no,student name,and three subjects marks such as c,c++,and python.
#calculate total marks,and percentage of marks,give grade=fail provided student secure<40 in any of the given subjects.
#Give grade=distinction provided studnet total marks lies with in 300 and 250
#Grade=First provided student total marks lies with in 249 and 200
#Grade=Second provided student total marks lies with in 199 and 150
#Grade=Third provided student total marks lies with in 149 and 120
#Display the total marks demo of the student.

stno=int(input("Enter studnet number:"))
sname=input("Enter student name:")
#validation of C marks
while(True):
    cm=int(input("Enter the marks of C:"))
    if(cm>=0)and (cm<=100):
        break
while(True):
    cpp=int(input("Enter the marks of CPP:"))
    if(cpp>=0)and (cpp<=100):
        break
while(True):
    py=int(input("Enter the marks of Python:"))
    if(py>=0)and (py<=100):
        break
#total and percentage.
print(cm,cpp,py)
total=cm+cpp+py
print(total)
avg=(total/300)*100
print(avg)
if(cm<40)or (cpp<40)or(py<40):
    grade="FAIL"
else:
    if(total<=300)and(total>=250):
        grade="DISTINCTION"       
    if (total<=249) and (total>=200):
        grade="FIRST"
    if (total<=199) and (total>=150):
        grade="SECOND"
    if (total<=149) and (total>=120):
        grade="THIRD"

#Display marks memo.
print("="*50)
print("\t Student marks Report")
print("="*60)
print("\t Student Number {}".format(stno))
print("\t Student Name {}".format(sname))
print("\t Student Marks in C {}".format(cm))
print("\t Student Marks in CPP {}".format(cpp))
print("\t Student Marks in Python {}".format(py))
print("="*60)
print("\t Student Total marks:{}".format(total))
print("\t Student Average marks:{}".format(avg))
print("-"*60)
print("\t Student grade:{}".format(grade))



    

    

