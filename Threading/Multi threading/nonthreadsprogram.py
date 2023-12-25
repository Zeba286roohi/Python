#nonthreadsprogram.py
import threading,time
def  squares(lst):
	print("Name of thread executing squares()=",threading.current_thread().name)
	for val in lst:
		print("square({})={}".format(val,val**2))
		time.sleep(1)

def  cubes(lst):
	print("Name of thread executing cubes()=",threading.current_thread().name)
	for val in lst:
		print("cubes({})={}".format(val,val**3))
		time.sleep(1)


#main program
bt=time.time()
print("Main Program Execution Started:")
tname=threading.current_thread().name
print("Name of main thread in main program=",tname)
print("-"*50)
lst=[2,5,6,3,8,9]
print("main thread came to main program going to squares()")
squares(lst)
print("main thread came to main program going to cubes()")
cubes(lst)
print("Main Program Execution Stoped:")
#find execution of this non-threading program
et=time.time()
print("\Execution time={}".format(et-bt))