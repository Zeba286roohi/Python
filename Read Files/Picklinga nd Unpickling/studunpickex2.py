#Program reading the record(s) from the file (use un-pickling)
#studunpickex2.py
import pickle
def   unpickleexample():
	try:
		with  open("pythstud.data", "rb") as fp:
			print("-"*50)
			print("Stno\tName\tMarks\tCname")
			print("-"*50)
			while(True):
				try:
					record=pickle.load(fp)
					for val in record:
						print("{}\t".format(val),end="")
					print()
				except EOFError:
					print("-"*50)
					break
	except FileNotFoundError:
		print("File does not exists:")

#main program
unpickleexample()
