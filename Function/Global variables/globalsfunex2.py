#globalsfunex2.py
a=10
b=20
c=30
d=40
def   operation():
	kvr=globals()   #  kvr  object---dict { Extrenal Global Varibles, 'a':10, 'b':20,'c':30,'d':40}
	print("type of kvr=",type(kvr))
	print("-------------------------------------")
	for k,v in kvr.items():
		print("{}----->{}".format(k,v))
	else:
		print("-------------------------------------")


#main program
operation()


"""
E:\KVR-PYTHON-9AM\FUNCTIONS>py globalsfunex2.py
type of kvr= <class 'dict'>
-------------------------------------
__name__----->__main__
__doc__----->None
__package__----->None
__loader__-----><_frozen_importlib_external.SourceFileLoader object at 0x000001F1151646A0>
__spec__----->None
__annotations__----->{}
__builtins__-----><module 'builtins' (built-in)>
__file__----->E:\KVR-PYTHON-9AM\FUNCTIONS\globalsfunex2.py
__cached__----->None
a----->10
b----->20
c----->30
d----->40
operation-----><function operation at 0x000001F114C93E20>
------------------------------------- """






