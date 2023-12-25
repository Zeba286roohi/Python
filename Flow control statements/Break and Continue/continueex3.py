#This Program find sum of +ve numbers and -ve numbers separately.
#continueex3.py
lst=[10,-20,30,40,-34,-45,89,-3,23,6]
ps=0
for val in lst:
	if(val<0):
		continue
	else:
		print("\t\t{}".format(val))
		ps=ps+val
else:
	print("Possitive Sum={}".format(ps))
	print("="*60)
	ns=0
	for val in lst:
		if(val>0):
			continue
		else:
			print("\t\t{}".format(val))
			ns=ns+val
	else:
		print("Negative Sum={}".format(ns))
		print("="*60)	


