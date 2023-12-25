import threading
def cube(num):
    print("Cube:{}".format(num*num*num))
def square(num):
    print("Sum:{}".format(num*num))

t1=threading.Thread(target=cube,args=(10,))
t2=threading.Thread(target=square,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
