#A Program for showing Inconsistant Result (or) non-thread safety result  in threading program
#NonLockingOopswithInh.py
import threading,time
class MulTable(threading.Thread):
	def  setvalue(self,n):
		self.n=n
	def run(self):
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

#main program
t1=MulTable()
t2=MulTable()
t3=MulTable()
t4=MulTable()
#set the values to the sub threads
t1.setvalue(3)
t2.setvalue(14)
t3.setvalue(20)
t4.setvalue(-13)
#dispatch the threads
t1.start()
t2.start()
t3.start()
t4.start()


