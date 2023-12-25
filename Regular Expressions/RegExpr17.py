#RegExpr17.py
#This program searches for space character
import re
mat=re.finditer("\s" , "$cWa BT#6AT&3pk @1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr17.py
==================================================
start index:4   End Index:5  Value:             (space)
start index:15   End Index:16  Value:          (space)
=================================================="""