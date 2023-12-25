#write a thread based application which will generate a multiplication table for a given number by using threads with oop approach.
#SecondApproachEx2.py
import threading,time
class MulTable(threading.Thread):
	def  run(self):  # overriding the run()
		self.n=int(input("Enter a number:"))
		if(self.n<=0):
			print("{} is invalid number:".format(self.n))
		else:
			print("-"*50)
			print("Mul Table for {}".format(self.n))
			print("-"*50)
			for i in range(1,11):
				print("\t{} x {} = {}".format(self.n,i,self.n*i))
				time.sleep(1)
			print("-"*50)

#main program
mt=MulTable()  # creating sub thread
mt.start()
