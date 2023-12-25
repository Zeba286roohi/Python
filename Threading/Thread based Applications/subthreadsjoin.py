#subthreadsjoin.py
import threading,time
def  fun1():
	print("Hi")
	time.sleep(10)

def   fun2(s):
	print("Hi, ",s)
	time.sleep(12)

#main program
print("Default Name of thread=",threading.current_thread().name) # Main Thread
t1=threading.Thread(target=fun1)  # here t1 is called sub thread
t2=threading.Thread(target=fun2,args=("Rossum", ))  # here t2 is called sub thread
print("Default Name of sub thread=", t1.name) # Thread-1
print("default Name of sub thread=", t2.name) # Thread-2
#assign User-Freindly Name to the sub threads
t1.name="Rossum"       #   t1.setName("Rossum")----is deprecated to an attribute "name"
t2.name="Ritche"         #    t2.setName("Ritche")----is deprecated to an attribute "name"
print("Name of sub thread=", t1.name) 
print("Name of sub thread=", t2.name)
print("\nNumber of threads active before start()=",threading.active_count()) # 1
print("Execution status of sub thread t1 before start()=", t1.is_alive()) # False
print("Execution status of sub thread t2 before start()=", t2.is_alive()) # False
t1.start()
t2.start()
print("\nNumber of threads active after start()=",threading.active_count()) # 3
print("Execution status of sub thread t1 after start()=", t1.is_alive()) # True
print("Execution status of sub thread t2 after start()=", t2.is_alive()) # True
#make the MainThread to wait until sub threads join.
t1.join()
t2.join()
print("\nLine-33:Number of threads active after completion of exec=",threading.active_count()) # 1
print("Execution status of sub thread t1 after completion of exec=", t1.is_alive()) # False
print("Execution status of sub thread t2 after completion of exec=", t2.is_alive()) # False