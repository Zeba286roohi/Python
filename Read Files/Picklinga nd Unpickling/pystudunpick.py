import pickle
try:
	with open("pythstud.data","rb") as fp:
		print("-"*50)
		print("Stno\tName\tMarks\tCname")
		print("-"*50)
		while(True):
			try:
				record=pickle.load(fp)  #   emprecord var of  <class, 'list'>
				for val in record:
					print("{}\t".format(val),end="")
				print()
			except EOFError:
				print("-"*50)
				break
except FileNotFoundError:
	print("File does not exists")
