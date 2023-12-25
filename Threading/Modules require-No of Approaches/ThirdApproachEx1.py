#ThirdApproachEx1.py
import threading  # step-1
class Test:    # Step-2
	def   hello(self,s): # step-3
		print("\nName of sub thread=",threading.current_thread().name)
		print("Hello ,{}, Good Morning".format(s))
		print("I am from hello() of Test Class")
		print("here hello() executed by sub thread")

#main program
t=Test() #  Create an object Programmer-defined class--step-4
subth=threading.Thread(target=t.hello, args=( ("Rossum",) ) )#  # create sub thread--Step-5
subth.start() #  # step-6

	