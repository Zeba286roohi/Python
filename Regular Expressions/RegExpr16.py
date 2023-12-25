#RegExpr16.py
#This program searches for all special symbols ( except alphabets and digits)
import re
mat=re.finditer("[^A-Za-z0-9]" , "$cWa BT#6A木T&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr16.py
==================================================
start index:0   End Index:1  Value:$
start index:4   End Index:5  Value:
start index:7   End Index:8  Value:#
start index:10   End Index:11  Value:木
start index:12   End Index:13  Value:&
start index:16   End Index:17  Value:@
=================================================="""