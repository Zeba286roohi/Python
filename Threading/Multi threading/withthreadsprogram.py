#withthreadsprogram.py
import threading,time
def  squares(lst):
	print("Name of thread executing squares()=",threading.current_thread().name) # Thread-1
	for val in lst:
		print("square({})={}".format(val,val**2))
		time.sleep(1)

def  cubes(lst):
	print("Name of thread executing cubes()=",threading.current_thread().name) # Thread-2
	for val in lst:
		print("cubes({})={}".format(val,val**3))
		time.sleep(1)


#main program
bt=time.time()
print("Main Program Execution Started:")
tname=threading.current_thread().name
print("Name of main thread in main program=",tname) # MainThread
print("-"*50)
lst=[2,5,6,3,8,9]
t1=threading.Thread(target=squares,args=(lst,) ) # here t1 is an object of Thread																											class--Therad-1
t2=threading.Thread(target=cubes,args=(lst,) ) # here t2 is an object of Thread																											class--Therad-2
t1.start()
t2.start()
t1.join()
t2.join()
print("Main Program Execution Completed:")
#find execution of this non-threading program
et=time.time()
print("\Execution time={}".format(et-bt))
