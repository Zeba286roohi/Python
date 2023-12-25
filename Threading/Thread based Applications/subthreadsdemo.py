#subthreadsdemo.py
import threading
def  fun1():
	print("Hi")

def   fun2(s):
	print("Hi, ",s)

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