#RegExpr21.py
#This program searching for all  digits
import re
mat=re.finditer("\d" , "$cWa BT#6AT-&3pk @1LH8bJ")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr21.py
==================================================
start index:8   End Index:9  Value:6
start index:13   End Index:14  Value:3
start index:18   End Index:19  Value:1
start index:21   End Index:22  Value:8
=================================================="""