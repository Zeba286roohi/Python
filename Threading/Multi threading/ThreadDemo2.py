#ThreadDemo2.py
import threading
def    fun1():
	print("i am from fun1()---executed by :",threading.current_thread().name)
def    fun2():
	print("i am from fun2()--executed by :",threading.current_thread().name)
def    fun3():
	print("i am from fun3()--executed by :",threading.current_thread().name)
def    fun4():
	print("i am from fun4()--executed by :",threading.current_thread().name)

#main program
print("Main Program Execution Started:")
tname=threading.current_thread().name
print("Name of main thread in main program=",tname)
print("-"*50)
fun1()
print("main thread came to main program going to fun2()")
fun2()
print("main thread came to main program going to fun3()")
fun3()
print("main thread came to main program going to fun4()")
fun4()
print("-"*50)
print("Main Program Execution stoped:")

