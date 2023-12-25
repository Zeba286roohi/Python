#RegExpr11.py
#This program searches for  all digits
import re
mat=re.finditer("[0-9]" , "cWaBT#6AT&3pk@1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr11.py
==================================================
start index:6   End Index:7  Value:6
start index:10   End Index:11  Value:3
start index:14   End Index:15  Value:1
start index:17   End Index:18  Value:8
=================================================="""