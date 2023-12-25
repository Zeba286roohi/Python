#StudentUnpick.py
import pickle
class StudentUnpick:
	def  readrecords(self):
		try:
			with open("stud.data","rb") as fp:
				print("="*50)
				print("\tStudent Details")
				print("="*50)
				while(True):
					try:
						obj=pickle.load(fp) # here obj is of type <<class 'Student.Student'>
						obj.dispstuddata()
					except EOFError:
						print("="*50)
						break
		except FileNotFoundError:
			print("File does not exists:")

#main program
su=StudentUnpick()
su.readrecords()