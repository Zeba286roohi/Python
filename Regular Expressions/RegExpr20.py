#RegExpr20.py
#This program searches for all sepcial symbhols except word character
import re
mat=re.finditer("\W" , "$cWa BT#6AT-&3pk @1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr20.py
==================================================
start index:0   End Index:1  Value:$
start index:4   End Index:5  Value:
start index:7   End Index:8  Value:#
start index:11   End Index:12  Value:&
start index:15   End Index:16  Value:
start index:16   End Index:17  Value:@
=================================================="""