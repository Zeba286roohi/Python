#program which will accept age of the citizen and decide whether it is elogible to vote or not.
'''basic program.
age=int(input("Enter the age of the citizen:"))
if(age>=18):
    print("Citizen is Eligible to vote")
else:
    print("Not Eligible to vote")'''

#high level
while(True):
    age=int(input("Enter the correct age of citizen:"))
    if(age>=18)and (age<=100):
         break
print("{} years old citizen is eligible to vote:".format(age))

    
    
