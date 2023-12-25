#StudentPick.py
import pickle
from Student import Student
class StudentPick:
	def  savestuddata(self):
		with open("stud.data","ab") as fp:
			#read the student data
			while(True):
				print("-"*50)
				stno=int(input("Enter Student Number:"))
				sname=input("Enter Student Name:")
				marks=float(input("Enter Student Marks:"))
				#create an object student class
				so=Student()
				so.setstudvalues(stno,sname,marks)
				#save or dump object so into the file
				pickle.dump(so,fp)
				print("-"*50)
				print("Student Records Saved in a File:")
				print("-"*50)
				ch=input("Do u want Insert another student Record(yes/no):")
				if(ch.lower()=="no"):
					break


#main program,
sp=StudentPick()
sp.savestuddata()

