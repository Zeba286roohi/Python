#A Program for showing Inconsistant Result (or) non-thread safety result  in threading program
#nonlockingFunctional.py
import time
import threading
def   multable(n):
	print("Name of Sub Thread in multable()=",threading.current_thread().name)
	if(n<=0):
		print("{} is invalid input".format(n))
	else:
		print("-"*50)
		print("Mul table for {}".format(n))
		print("-"*50)
		for i in range(1,11):
			print("\t{} x {} = {}".format(n,i,n*i))
			time.sleep(1)
		print("-"*50)

#main program
t1=threading.Thread(target=multable,args=((6,)) )
t2=threading.Thread(target=multable,args=((16,)) )
t3=threading.Thread(target=multable,args=((19,)) )
t4=threading.Thread(target=multable,args=((14,)) )
t1.start()
t2.start()
t3.start()
t4.start()