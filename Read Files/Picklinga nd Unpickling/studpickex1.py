#Program for accepting no of students details such as stdno, stdname, marks and college name and save them in a file (use pickling)
#studpickex1.py
import pickle
with open("pythstud.data", "ab") as fp:
	nos=int(input("Enter how many students u have:"))
	if(nos<=0):
		print("Invalid input:")
	else:
		for i in range(1,nos+1):#no change if use nos
			print("-"*50)
			print("Enter {} Student Information:".format(i))
			print("-"*50)
			#accept student values
			stno=int(input("Enter Student Number:"))
			sname=input("Enter Student Name:")
			marks=float(input("Enter Student Marks:"))
			cname=input("Enter Student College Name:")
			#create an object 
			lst=list()  # create an empty list
			#append student data
			lst.append(stno)
			lst.append(sname)
			lst.append(marks)
			lst.append(cname)
			#write object data to the file
			pickle.dump(lst,fp)
			print("-"*50)
			print("{} Student  data saved successfully in File".format(i))













