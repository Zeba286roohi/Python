#SecondApproachEx1.py
import threading   # step-1
#       step-2          step-3
class Sample(threading.Thread):
	def  run(self):  # step-4
		print("\nName of sub thread=",threading.current_thread().name)
		print("i am from run()")

		
#main program
print("Default Name of thread=",threading.current_thread().name) #MainThread
#create a sub thread
t1=Sample()
t1.name="OOPS"
print("Is sub thread alive before start=",t1.is_alive())#False
t1.start()
print("Is sub thread alive after start=",t1.is_alive())#True

