#A Program for showing Inconsistant Result (or) non-thread safety result  in threading program
#LockingOopswithoutInhex1.py
import threading,time
class MulTable:
	@classmethod
	def  getlock(cls):
		cls.KVR=threading.Lock()  # creating a lock on the name of "KVR"---Step-1
	def __init__(self):
		self.n=int(input("Enter a Number for Mul Table:"))
	def table(self):
		MulTable.KVR.acquire() #Step-2
		print("Name of Sub Thread in run()=",threading.current_thread().name)
		if(self.n<=0):
			print("{} is invalid input".format(self.n))
		else:
			print("-"*50)
			print("Mul table for {}".format(self.n))
			print("-"*50)
			for i in range(1,11):
				print("\t{} x {} = {}".format(self.n,i,self.n*i))
				time.sleep(1)
			print("-"*50)
		MulTable.KVR.release()  #Step-3
	
#main program
MulTable.getlock() # Calling Class Level Method
t1=MulTable()
t2=MulTable()
t3=MulTable()
t4=MulTable()
#create sub threads
st1=threading.Thread(target=t1.table)
st2=threading.Thread(target=t2.table)
st3=threading.Thread(target=t3.table)
st4=threading.Thread(target=t4.table)

#dispatch the threads
st1.start()
st2.start()
st3.start()
st4.start()


