#sharesdemo.py
import shares,time,importlib
def   disp(d):
	print("="*50)
	print("\tShare Name\tShare Value:")
	print("="*50)
	for sn,sv in d.items():
		print("\t{}\t\t{}".format(sn,sv))
	print("="*50)
#main program
d=shares.sharesinfo()
disp(d)
print("i am going to sleep")
time.sleep(20)
print("i am coming out of sleep:")
importlib.reload(shares)
d=shares.sharesinfo()
disp(d)
