#ThirdApproachEx2.py
import threading  # step-1
import time
class Roohi:    # Step-2
	def  table(self,n):  # step-3
		if(n<=0):
			print("{} is invalid input:".format(n))
		else:
			print("="*50)
			print("Mul Table for :{}".format(n))
			print("="*50)
			for i in range(1,11):
				print("\t{} x {} = {}".format(n,i,n*i))
				time.sleep(1)
			print("="*50)

#main program
R=Roohi() # Create an object Programmer-defined class--step-4
t1=threading.Thread(target=R.table,args=( (int(input("Enter a number:")),) )  )  # create sub thread--Step-5
t1.start()  # step-6