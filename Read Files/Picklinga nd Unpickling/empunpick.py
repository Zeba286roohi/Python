#Program for reading all the records from file by using un-pickling 
#empunpick.py
import pickle
try:
	with open("emp.data","rb") as fp:
		print("-"*50)
		print("Employee Details")
		print("-"*50)
		while(True):
			try:
				emprecord=pickle.load(fp)  #   emprecord var of  <class, 'list'>
				for val in emprecord:
					print("{}\t".format(val),end="")
				print()
			except EOFError:
				print("-"*50)
				break
except FileNotFoundError:
	print("File does not exists")