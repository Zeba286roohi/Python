#continueex1.py
s="PYTHON"      
# want to display    PYTON  
for v in s:
	if(v=="H"):
		continue
	else:
		print("\t{}".format(v))
else:
	print("else part of for loop")
print("-"*60)
# want to display    PYTN  
for v in s:
	if(v=="H") or(v=="O"):
		continue
	else:
		print("\t{}".format(v))

